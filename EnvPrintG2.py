# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def disegnaAmbiente(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, numStanza, listaNemici, caricaTutto):
    if caricaTutto:
        schermo.blit(imgSfondoStanza, (0, 0))
        # porte
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
        # cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                        caseviste[j] == cofanetti[i + 1] + gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - gpy) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + gpy)) and \
                        caseviste[j + 2]:
                    schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                    if cofanetti[i + 3]:
                        schermo.blit(cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        schermo.blit(cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j = j + 3
            i = i + 4
        i = 0
        # disegno le caselle viste
        while i < len(caseviste):
            if caseviste[i + 2]:
                n = 0
                while n < 32:
                    if caseviste[i] == gpx * n:
                        m = 0
                        while m < 18:
                            if caseviste[i + 1] == gpy * m:
                                if (n + m) % 2 == 0:
                                    schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                                if (n + m) % 2 != 0:
                                    schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                            m = m + 1
                    n = n + 1
            i = i + 3

    # disegnare casella sopra la vecchia posizione dei personaggi e mostri
    n = 0
    while n < 32:
        if vx == gpx * n:
            m = 0
            while m < 18:
                if vy == gpy * m:
                    if (n + m) % 2 == 0:
                        schermo.blit(sfondinoa, (vx, vy))
                    if (n + m) % 2 != 0:
                        schermo.blit(sfondinob, (vx, vy))
                m = m + 1
        n = n + 1
    n = 0
    while n < 32:
        if vrx == gpx * n:
            m = 0
            while m < 18:
                if vry == gpy * m:
                    if (n + m) % 2 == 0:
                        schermo.blit(sfondinoa, (vrx, vry))
                    if (n + m) % 2 != 0:
                        schermo.blit(sfondinob, (vrx, vry))
                m = m + 1
        n = n + 1
    j = 0
    while j < len(caseviste):
        for nemico in listaNemici:
            if caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                n = 0
                while n < 32:
                    if nemico.vx == gpx * n:
                        m = 0
                        while m < 18:
                            if nemico.vy == gpy * m:
                                if (n + m) % 2 == 0:
                                    schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                                if (n + m) % 2 != 0:
                                    schermo.blit(sfondinob, (nemico.vx, nemico.vy))
                            m = m + 1
                    n = n + 1
        j = j + 3

    # backbround occhio/chiave
    schermo.blit(sfochiaveocchio, (gsx - (gpx * 5), 0))

    # vista nemici
    if apriocchio:
        schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
    else:
        schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))

    # chiave robo
    if chiamarob:
        schermo.blit(chiaveroboacc, (gsx - (gpx * 4), 0))
    else:
        schermo.blit(chiaverobospe, (gsx - (gpx * 4), 0))

    # esche: id, vita, xesca, yesca
    i = 0
    while i < len(vitaesca):
        schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
        i = i + 4

    # robo
    schermo.blit(robot, (rx, ry))
    if surrisc > 0:
        schermo.blit(roboSurrisc, (rx, ry))
    schermo.blit(armrob, (rx, ry))

    # personaggio
    if npers == 1:
        schermo.blit(scudo, (x, y))
        schermo.blit(pers, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(persdb, (x, y))
        schermo.blit(arma, (x, y))
    if npers == 2:
        schermo.blit(arma, (x, y))
        schermo.blit(pers, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(persab, (x, y))
        schermo.blit(scudo, (x, y))
    if npers == 3:
        schermo.blit(arma, (x, y))
        schermo.blit(scudo, (x, y))
        schermo.blit(pers, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(perswb, (x, y))
    if npers == 4:
        schermo.blit(pers, (x, y))
        if avvele:
            schermo.blit(persAvvele, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(perssb, (x, y))
        schermo.blit(arma, (x, y))
        schermo.blit(scudo, (x, y))

    # vita-status personaggio
    lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
    fineindvitapers = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
    vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
    schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(fineindvitapers, ((gsx // 32 * 1) + lungvitatot, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 16))
    persbat = pygame.transform.scale(perso, (gpx, gpy))
    schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 16))
    schermo.blit(perssb, (gsx // 32 * 0, gsy // 18 * 16))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if attp > 0:
        schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
    if difp > 0:
        schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

    # vita-status robo
    lungentot = int(((gpx * entot) / float(4)) // 10)
    lungen = (lungentot * enrob) // entot
    if lungen < 0:
        lungen = 0
    indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
    fineindvitarob = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
    vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
    schermo.blit(indvitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(fineindvitarob, ((gsx // 32 * 1) + lungentot, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(vitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 17))
    robobat = pygame.transform.scale(roboo, (gpx, gpy))
    schermo.blit(robobat, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if surrisc > 0:
        schermo.blit(surriscaldato, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if velp > 0:
        schermo.blit(velocitapiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
    if effp > 0:
        schermo.blit(efficienzapiu, ((gsx // 32 * 1) + (gpx // 4 * 3) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))

    # disegnare i mostri
    j = 0
    while j < len(caseviste):
        for nemico in listaNemici:
            if not nemico.morto and caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                if nemico.appiccicato:
                    schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                if nemico.avvelenato:
                    schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
        j = j + 3

    pygame.display.update()


def attacca(x, y, npers, nrob, rx, ry, pers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, stanzaa, stanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob, attVicino, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici):
    xp = x
    yp = y
    nxp = 0
    nyp = 0
    risposta = False
    difesa = 0

    # modifica puntatore a seconda dell'attacco
    if attacco == 1:
        puntatogg1 = puntatDif
        puntatogg2 = puntatAtt
        puntatogg3 = puntatPor
        puntatogg4 = puntatSpinta
        puntatogg5 = puntatCof
    if attacco == 2:
        puntatogg = puntatBom
    if attacco == 3:
        puntatogg = puntatBoV
    if attacco == 4:
        puntatogg = puntatEsc
    if attacco == 5:
        puntatogg = puntatBoA
    if attacco == 6:
        puntatogg = puntatBoP

    schermo.blit(stanzaa, (0, 0))
    # backbround occhio/chiave
    schermo.blit(sfochiaveocchio, (gsx - (gpx * 5), 0))

    # vista nemici
    if apriocchio:
        schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
    else:
        schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))

    # chiave robo
    if chiamarob:
        schermo.blit(chiaveroboacc, (gsx - (gpx * 4), 0))
    else:
        schermo.blit(chiaverobospe, (gsx - (gpx * 4), 0))
    # porte
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            vmurx = porte[i + 1]
            vmury = porte[i + 2]
            murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, stanza, False, False, False, porte, cofanetti)
            schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
            if vmurx == murx and vmury == mury:
                schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
            else:
                schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
        i = i + 4
    # cofanetti
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
            j = j + 3
        i = i + 4
    i = 0
    # disegno le caselle viste
    while i < len(caseviste):
        if caseviste[i + 2]:
            n = 0
            while n < 32:
                if caseviste[i] == gpx * n:
                    m = 0
                    while m < 18:
                        if caseviste[i + 1] == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                        m = m + 1
                n = n + 1
        i = i + 3

    # vita-status personaggio
    lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
    fineindvitapers = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
    vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
    schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(fineindvitapers, ((gsx // 32 * 1) + lungvitatot, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 16))
    persbat = pygame.transform.scale(perso, (gpx, gpy))
    schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 16))
    schermo.blit(perssb, (gsx // 32 * 0, gsy // 18 * 16))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if attp > 0:
        schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
    if difp > 0:
        schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

    # vita-status robo
    lungentot = int(((gpx * entot) / float(4)) // 10)
    lungen = (lungentot * enrob) // entot
    if lungen < 0:
        lungen = 0
    indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
    fineindvitarob = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
    vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
    schermo.blit(indvitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(fineindvitarob, ((gsx // 32 * 1) + lungentot, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(vitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 17))
    robobat = pygame.transform.scale(roboo, (gpx, gpy))
    schermo.blit(robobat, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if surrisc > 0:
        schermo.blit(surriscaldato, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if velp > 0:
        schermo.blit(velocitapiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
    if effp > 0:
        schermo.blit(efficienzapiu, ((gsx // 32 * 1) + (gpx // 4 * 3) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))

    tastotempfps = 3
    tastop = 0
    numTastiPremuti = 0
    danno = 0
    creaesca = False
    ricaricaschermo = False
    appenaCaricato = False
    suPorta = False
    suCofanetto = False
    apriChiudiPorta = [False, 0, 0]
    apriCofanetto = [False, 0, 0]
    spingiColco = False
    mvx = 0
    mvy = 0
    puntaPorta = False
    puntaCofanetto = False
    attaccato = False
    while not risposta:
        xvp = xp
        yvp = yp

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
            nxp = 0
            nyp = 0
        if tastotempfps == 0 and tastop != 0:
            if tastop == pygame.K_w:
                nyp = -gpy
            if tastop == pygame.K_a:
                nxp = -gpx
            if tastop == pygame.K_s:
                nyp = gpy
            if tastop == pygame.K_d:
                nxp = gpx
            tastotempfps = 2
            xvp = xp
            yvp = yp

        n = 0
        while n < 32:
            if xvp == gpx * n:
                m = 0
                while m < 18:
                    if yvp == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (xvp, yvp))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (xvp, yvp))
                    m = m + 1
            n = n + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                appenaCaricato = False
                # esci
                if event.key == pygame.K_q:
                    risposta = True
                    sposta = False
                    canaleSoundPuntatore.play(selind)
                # movimento puntatore
                tastop = event.key
                if event.key == pygame.K_w:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nyp = -gpy
                    nxp = 0
                if event.key == pygame.K_a:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nxp = -gpx
                    nyp = 0
                if event.key == pygame.K_s:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nyp = gpy
                    nxp = 0
                if event.key == pygame.K_d:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nxp = gpx
                    nyp = 0
                # attacco
                if event.key == pygame.K_SPACE:
                    sposta = False
                    if attacco != 0:
                        infliggidanno = False
                        statom = 0
                        raggio = 0
                        # spingi Colco attacco = 1
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and (xp == rx and yp == ry):
                            spingiColco = True
                            sposta = True
                            risposta = True
                        # apri/chiudi porta attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and suPorta:
                            apriChiudiPorta = [True, xp, yp]
                            sposta = True
                            risposta = True
                        # apri cofanetto attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and suCofanetto:
                            apriCofanetto = [True, xp, yp]
                            sposta = True
                            risposta = True
                        # normale attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)):
                            infliggidanno = True
                            danno = attVicino
                            raggio = gpx * 0
                        # difesa attacco = 1
                        elif attacco == 1 and (xp == x and yp == y):
                            difesa = 2
                            risposta = True
                        # bomba attacco = 2
                        if attacco == 2 and (abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6):
                            attaccato = True
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 10
                                raggio = gpx * 1
                                sposta = True
                                risposta = True
                        # bomba veleno attacco = 3
                        if attacco == 3 and (abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5):
                            attaccato = True
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 20
                                statom = 1
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # esca attacco = 4
                        if attacco == 4 and (abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6):
                            attaccato = True
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                # conferma lancio esche
                                confesca = True
                                i = 2
                                while i < len(vitaesca):
                                    if vitaesca[i] == xp and vitaesca[i + 1] == yp:
                                        confesca = False
                                    i = i + 4
                                for nemico in listaNemici:
                                    if nemico.x == xp and nemico.y == yp:
                                        confesca = False
                                        break
                                if confesca:
                                    infliggidanno = True
                                    danno = 0
                                    raggio = 0
                                    creaesca = True
                                    sposta = True
                                    risposta = True
                                else:
                                    canaleSoundPuntatore.play(selimp)
                        # bomba appiccicosa attacco = 5
                        if attacco == 5 and (abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5):
                            attaccato = True
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 20
                                statom = 2
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # bomba potenziata attacco = 6
                        if attacco == 6 and (abs(x - xp) <= gpx * 4 and abs(y - yp) <= gpy * 4):
                            attaccato = True
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 200
                                raggio = gpx * 2
                                sposta = True
                                risposta = True

                        for nemico in listaNemici:
                            if (((abs(nemico.x - xp) <= raggio and abs(nemico.y - yp) <= raggio) and attacco != 1) or ((xp == nemico.x and yp == nemico.y) and attacco == 1)) and infliggidanno:
                                if statom == 1:
                                    nemico.avvelenato = True
                                if statom == 2:
                                    nemico.appiccicato = True
                                nemico.danneggia(danno, "Rallo")
                                sposta = True
                                risposta = True

                        # attacco normale se c'e' il mostro
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and sposta and risposta:
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                        # attacco normale se non c'e' il mostro
                        """elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and not sposta and not risposta:
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                            sposta = True
                            risposta = True"""

                        if not risposta:
                            canaleSoundPuntatore.play(selimp)
            if event.type == pygame.KEYUP:
                if tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d:
                    numTastiPremuti -= 1
                    if event.key == tastop:
                        numTastiPremuti = 0
                else:
                    numTastiPremuti = 0
                if numTastiPremuti == 0:
                    tastop = 0
                    tastotempfps = 5
                    nxp = 0
                    nyp = 0

        if ricaricaschermo and not appenaCaricato:
            schermo.blit(stanzaa, (0, 0))
            # porte
            i = 0
            while i < len(porte):
                if not porte[i + 3]:
                    vmurx = porte[i + 1]
                    vmury = porte[i + 2]
                    murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, stanza, False, False, False, porte, cofanetti)
                    schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
                    if vmurx == murx and vmury == mury:
                        schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
                    else:
                        schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
                i = i + 4
            # cofanetti
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
                    j = j + 3
                i = i + 4
            # background occhio/chiave
            schermo.blit(sfochiaveocchio, (gsx - (gpx * 5), 0))
            # vista nemici
            if apriocchio:
                schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
            else:
                schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))
            # chiave robo
            if chiamarob:
                schermo.blit(chiaveroboacc, (gsx - (gpx * 4), 0))
            else:
                schermo.blit(chiaverobospe, (gsx - (gpx * 4), 0))
            # fai vedere stanze visitate
            # caseviste[x, y, flag, ... ] -> riempito come se non vedessi niente
            i = 0
            # disegno le caselle viste
            while i < len(caseviste):
                if caseviste[i + 2]:
                    n = 0
                    while n < 32:
                        if caseviste[i] == gpx * n:
                            m = 0
                            while m < 18:
                                if caseviste[i + 1] == gpy * m:
                                    if (n + m) % 2 == 0:
                                        schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                                    if (n + m) % 2 != 0:
                                        schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                                m = m + 1
                        n = n + 1
                i = i + 3
            ricaricaschermo = False
            appenaCaricato = True

        # disegna porte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                vmurx = porte[i + 1]
                vmury = porte[i + 2]
                murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, stanza, False, False, False, porte, cofanetti)
                schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
                if vmurx == murx and vmury == mury:
                    schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
                else:
                    schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
            i = i + 4
        # disegna cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                        caseviste[j] == cofanetti[i + 1] + gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - gpy) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + gpy)) and \
                        caseviste[j + 2]:
                    schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                    if cofanetti[i + 3]:
                        schermo.blit(cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        schermo.blit(cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j = j + 3
            i = i + 4

        # visualizza campo attaccabile
        if attacco == 1:
            schermo.blit(campoattaccabile1, (x - gpx, y - gpy))
            # controllo caselle attaccabili
            caseattactot = [x + gpx, y, True, x - gpx, y, True, x, y + gpy, True, x, y - gpy, True]
            murx = x
            mury = y
            nmurx, nmury, stanza, inutile, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[2] = False
                i = 0
                while i < len(porte):
                    if murx + gpx == porte[i + 1] and mury == porte[i + 2]:
                        caseattactot[2] = True
                    i = i + 4
                i = 0
                while i < len(cofanetti):
                    if murx + gpx == cofanetti[i + 1] and mury == cofanetti[i + 2]:
                        caseattactot[2] = True
                    i = i + 4
            murx = x
            mury = y
            nmurx, nmury, stanza, inutile, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[5] = False
                i = 0
                while i < len(porte):
                    if murx - gpx == porte[i + 1] and mury == porte[i + 2]:
                        caseattactot[5] = True
                    i = i + 4
                i = 0
                while i < len(cofanetti):
                    if murx - gpx == cofanetti[i + 1] and mury == cofanetti[i + 2]:
                        caseattactot[5] = True
                    i = i + 4
            murx = x
            mury = y
            nmurx, nmury, stanza, inutile, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[8] = False
                i = 0
                while i < len(porte):
                    if murx == porte[i + 1] and mury + gpy == porte[i + 2]:
                        caseattactot[8] = True
                    i = i + 4
                i = 0
                while i < len(cofanetti):
                    if murx == cofanetti[i + 1] and mury + gpy == cofanetti[i + 2]:
                        caseattactot[8] = True
                    i = i + 4
            murx = x
            mury = y
            nmurx, nmury, stanza, inutile, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[11] = False
                i = 0
                while i < len(porte):
                    if murx == porte[i + 1] and mury - gpy == porte[i + 2]:
                        caseattactot[11] = True
                    i = i + 4
                i = 0
                while i < len(cofanetti):
                    if murx == cofanetti[i + 1] and mury - gpy == cofanetti[i + 2]:
                        caseattactot[11] = True
                    i = i + 4
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2]:
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 2:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (x - (gpx * 6), y - (gpy * 6)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 6 and caseattactot[i + 1] <= y + gpy * 6 and caseattactot[i] >= x - gpx * 6 and caseattactot[i + 1] >= y - gpy * 6 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 3:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 11, gpy * 11))
            schermo.blit(campoattaccabile3, (x - (gpx * 5), y - (gpy * 5)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 5 and caseattactot[i + 1] <= y + gpy * 5 and caseattactot[i] >= x - gpx * 5 and caseattactot[i + 1] >= y - gpy * 5 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 4:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (x - (gpx * 6), y - (gpy * 6)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 6 and caseattactot[i + 1] <= y + gpy * 6 and caseattactot[i] >= x - gpx * 6 and caseattactot[i + 1] >= y - gpy * 6 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 5:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 11, gpy * 11))
            schermo.blit(campoattaccabile3, (x - (gpx * 5), y - (gpy * 5)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 5 and caseattactot[i + 1] <= y + gpy * 5 and caseattactot[i] >= x - gpx * 5 and caseattactot[i + 1] >= y - gpy * 5 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 6:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 9, gpy * 9))
            schermo.blit(campoattaccabile3, (x - (gpx * 4), y - (gpy * 4)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 4 and caseattactot[i + 1] <= y + gpy * 4 and caseattactot[i] >= x - gpx * 4 and caseattactot[i + 1] >= y - gpy * 4 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3

        # mettere il puntatore su porte
        i = 0
        while i < len(porte):
            if porte[i + 1] == xp + nxp and porte[i + 2] == yp + nyp and not porte[i + 3]:
                puntaPorta = True
                xp = xp + nxp
                yp = yp + nyp
                nxp = 0
                nyp = 0
                break
            i = i + 4
        # mettere il puntatore su cofanetti
        puntaCofanetto = False
        i = 0
        while i < len(cofanetti):
            if cofanetti[i + 1] == xp + nxp and cofanetti[i + 2] == yp + nyp:
                puntaCofanetto = True
                xp = xp + nxp
                yp = yp + nyp
                break
            i = i + 4
        # movimento inquadra (ultimi 4 inutili)
        if not puntaPorta and not puntaCofanetto:
            xp, yp, stanza, inutile, cambiosta = muri_porte(xp, yp, nxp, nyp, stanza, False, True, False, porte, cofanetti)
        # movimento inquadra quando si è sulle porte
        if puntaPorta:
            i = 0
            while i < len(caseviste):
                if caseviste[i] == xp + nxp and caseviste[i + 1] == yp + nyp:
                    if caseviste[i + 2]:
                        xp = xp + nxp
                        yp = yp + nyp
                        puntaPorta = False
                        break
                i = i + 3

        # esche: id, vita, xesca, yesca
        i = 0
        while i < len(vitaesca):
            schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
            i = i + 4

        # robo
        schermo.blit(robot, (rx, ry))
        if surrisc > 0:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
        # personaggio
        if not risposta:
            if npers == 1:
                schermo.blit(scudo, (x, y))
                schermo.blit(pers, (x, y))
                if avvele:
                    schermo.blit(persAvvele, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(persdb, (x, y))
                schermo.blit(arma, (x, y))
            if npers == 2:
                schermo.blit(arma, (x, y))
                schermo.blit(pers, (x, y))
                if avvele:
                    schermo.blit(persAvvele, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(persab, (x, y))
                schermo.blit(scudo, (x, y))
            if npers == 3:
                schermo.blit(arma, (x, y))
                schermo.blit(scudo, (x, y))
                schermo.blit(pers, (x, y))
                if avvele:
                    schermo.blit(persAvvele, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(perswb, (x, y))
            if npers == 4:
                schermo.blit(pers, (x, y))
                if avvele:
                    schermo.blit(persAvvele, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(perssb, (x, y))
                schermo.blit(arma, (x, y))
                schermo.blit(scudo, (x, y))

        # disegnare i mostri
        j = 0
        while j < len(caseviste):
            for nemico in listaNemici:
                if caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                    schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.appiccicato:
                        schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.avvelenato:
                        schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
                    break
            j = j + 3

        # puntatore
        if attacco == 1:
            puntatogg = 0
            if (xp == x) and (yp == y):
                suPorta = False
                suCofanetto = False
                puntatogg = puntatogg1
            elif (xp == rx) and (yp == ry):
                suPorta = False
                suCofanetto = False
                puntatogg = puntatogg4
            else:
                suPorta = False
                suCofanetto = False
                i = 0
                while i < len(porte):
                    if (xp == porte[i + 1]) and (yp == porte[i + 2]):
                        suPorta = True
                        puntatogg = puntatogg3
                        break
                    i = i + 4
                i = 0
                while i < len(cofanetti):
                    if (xp == cofanetti[i + 1]) and (yp == cofanetti[i + 2]):
                        if not cofanetti[i + 3]:
                            suCofanetto = True
                            puntatogg = puntatogg5
                        break
                    i = i + 4
                puntandoNemico = False
                for nemico in listaNemici:
                    if xp == nemico.x and yp == nemico.y:
                        puntandoNemico = True
                        break
                if not suPorta and not suCofanetto and puntandoNemico:
                    puntatogg = puntatogg2
            if ((xp == x and yp == y) or (xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and puntatogg != 0:
                puntat = puntatIn
            else:
                puntat = puntatOut
        if attacco == 2:
            if abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6:
                puntat = puntatIn
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 3:
            if abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5:
                puntat = puntatIn
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 4:
            if abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6:
                puntat = puntatIn
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 5:
            if abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5:
                puntat = puntatIn
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 6:
            if abs(x - xp) <= gpx * 4 and abs(y - yp) <= gpy * 4:
                puntat = puntatIn
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        schermo.blit(puntat, (xp, yp))
        if puntatogg != 0:
            schermo.blit(puntatogg, (xp, yp))
        if risposta:
            n = 0
            m = 0
            while n < 32:
                if xp == gpx * n:
                    while m < 18:
                        if yp == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (xp, yp))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (xp, yp))
                        m = m + 1
                n = n + 1

        # disegna vita-status-raggio visivo mostri
        for nemico in listaNemici:
            mx = nemico.x
            my = nemico.y
            pvm = nemico.vita
            pvmtot = nemico.vitaTotale
            raggiovista = nemico.raggioVisivo
            if xp == mx and yp == my:
                # controllo caselle attaccabili
                caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
                i = 0
                # disegno le caselle attaccabili
                while i < len(caseattactot):
                    if not caseattactot[i + 2] and (caseattactot[i] <= mx + raggiovista and caseattactot[i + 1] <= my + raggiovista and caseattactot[i] >= mx - raggiovista and caseattactot[i + 1] >= my - raggiovista and not (caseattactot[i] == mx and caseattactot[i + 1] == my)):
                        schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovista * 2) + gpx, (raggiovista * 2) + gpy))
                schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
                schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
                schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
                if nemico.avvelenato:
                    schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
                if nemico.appiccicato:
                    schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
                schermo.blit(nemico.imgAttuale, (gsx // 32 * 1, gpy // 3))
                fineindvitamost = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
                if pvmtot > 1500:
                    indvitamost = pygame.transform.scale(indvita, (int(((gpx * 1500) / float(4)) // 15), gpy // 4))
                    schermo.blit(fineindvitamost, ((gsx // 32 * 2) + 1500, gpy // 3))
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
                    schermo.blit(fineindvitamost, ((gsx // 32 * 2) + lungvitatot, gpy // 3))
                    vitanemsucc = pygame.transform.scale(vitanemico00, ((gpx // 4) * (lungvitatot // 15), gpy // 4))
                    vitanemico = vitanemico0
                lungvita = int(((gpx * pvm) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
                schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
                schermo.blit(vitanemsucc, (gsx // 32 * 2, gpy // 3))
                schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
                ricaricaschermo = True
                if (mx != mvx) or (my != mvy):
                    appenaCaricato = False
                mvx = mx
                mvy = my
            j += 7

        for nemico in listaNemici:
            if not (xp == nemico.x and yp == nemico.y):
                ricaricaschermo = False
                if xvp == nemico.x and yvp == nemico.y:
                    ricaricaschermo = True
                    appenaCaricato = False
                    break

        # backbround occhio/chiave
        schermo.blit(sfochiaveocchio, (gsx - (gpx * 5), 0))
        # vista nemici
        if apriocchio:
            schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
        else:
            schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))
        # chiave robo
        if chiamarob:
            schermo.blit(chiaveroboacc, (gsx - (gpx * 4), 0))
        else:
            schermo.blit(chiaverobospe, (gsx - (gpx * 4), 0))

        # disegna vita esche
        i = 0
        while i < len(vitaesca):
            if xp == vitaesca[i + 2] and yp == vitaesca[i + 3]:
                lungvita = (gpx * 8 * vitaesca[i + 1]) // 100
                if lungvita < 0:
                    lungvita = 0
                schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
                schermo.blit(esche, (gsx // 32 * 1, gpy // 3))
                indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
                fineindvitamost = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
                vitaesche = pygame.transform.scale(vitanemico0, (lungvita, gpy // 4))
                schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
                schermo.blit(fineindvitamost, ((gsx // 32 * 2) + (gpx * 8), gpy // 3))
                schermo.blit(vitaesche, (gsx // 32 * 2, gpy // 3))
                ricaricaschermo = True
            i = i + 4

        # vita-status personaggio
        lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
        lungvita = (lungvitatot * pv) // pvtot
        if lungvita < 0:
            lungvita = 0
        indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
        fineindvitapers = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
        vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
        schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
        schermo.blit(fineindvitapers, ((gsx // 32 * 1) + lungvitatot, (gsy // 18 * 16) + (gpy // 4 * 3)))
        schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
        schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 16))
        persbat = pygame.transform.scale(perso, (gpx, gpy))
        schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 16))
        schermo.blit(perssb, (gsx // 32 * 0, gsy // 18 * 16))
        schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
        if avvele:
            schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
        if attp > 0:
            schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
        if difp > 0:
            schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

        # vita-status-campo visivo robo
        lungentot = int(((gpx * entot) / float(4)) // 10)
        lungen = (lungentot * enrob) // entot
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
        fineindvitarob = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
        vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
        schermo.blit(indvitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
        schermo.blit(fineindvitarob, ((gsx // 32 * 1) + lungentot, (gsy // 18 * 17) + (gpy // 4 * 3)))
        schermo.blit(vitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
        schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 17))
        robobat = pygame.transform.scale(roboo, (gpx, gpy))
        schermo.blit(robobat, (gsx // 32 * 0, gsy // 18 * 17))
        schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
        if surrisc > 0:
            schermo.blit(surriscaldato, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
        if velp > 0:
            schermo.blit(velocitapiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
        if effp > 0:
            schermo.blit(efficienzapiu, ((gsx // 32 * 1) + (gpx // 4 * 3) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
        if xp == rx and yp == ry and enrob > 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
            raggiovista = gpx * 6
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= rx + raggiovista and caseattactot[i + 1] <= ry + raggiovista and caseattactot[i] >= rx - raggiovista and caseattactot[i + 1] >= ry - raggiovista and not (caseattactot[i] == rx and caseattactot[i + 1] == ry)):
                    schermo.blit(caselleattaccabiliRobo, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabileRobo, ((raggiovista * 2) + gpx, (raggiovista * 2) + gpy))
            schermo.blit(campoattaccabile3, (rx - raggiovista, ry - raggiovista))
            ricaricaschermo = True
            if (rx != mvx) or (ry != mvy):
                appenaCaricato = False

        if not risposta:
            pygame.display.update()
        elif not sposta or not attaccato:
            attacco = 0
        pygame.event.pump()
        clockAttacco.tick(fpsInquadra)

    return sposta, creaesca, xp, yp, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco
