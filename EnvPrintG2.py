# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def disegnaAmbiente(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, numStanza, listaNemici, caricaTutto, vettoreDenaro, numFrecce, nemicoInquadrato):
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
                    break
                j = j + 3
            i = i + 4
        # disegno le caselle viste
        i = 0
        while i < len(caseviste):
            if caseviste[i + 2]:
                if ((caseviste[i] / gpx) + (caseviste[i + 1] / gpy)) % 2 == 0:
                    schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                if ((caseviste[i] / gpx) + (caseviste[i + 1] / gpy)) % 2 == 1:
                    schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
            i += 3

    # disegnare casella sopra la vecchia posizione dei personaggi e mostri
    if ((vx / gpx) + (vy / gpy)) % 2 == 0:
        schermo.blit(sfondinoa, (vx, vy))
    if ((vx / gpx) + (vy / gpy)) % 2 == 1:
        schermo.blit(sfondinob, (vx, vy))
    if ((vrx / gpx) + (vry / gpy)) % 2 == 0:
        schermo.blit(sfondinoa, (vrx, vry))
    if ((vrx / gpx) + (vry / gpy)) % 2 == 1:
        schermo.blit(sfondinob, (vrx, vry))
    j = 0
    while j < len(caseviste):
        for nemico in listaNemici:
            if caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                if ((nemico.vx / gpx) + (nemico.vy / gpy)) % 2 == 0:
                    schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                if ((nemico.vx / gpx) + (nemico.vy / gpy)) % 2 == 1:
                    schermo.blit(sfondinob, (nemico.vx, nemico.vy))
        j += 3

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

    # denaro: qta, x, y
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

    # robo
    schermo.blit(robot, (rx, ry))
    if surrisc > 0:
        schermo.blit(roboSurrisc, (rx, ry))
    schermo.blit(armrob, (rx, ry))

    disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

    # vita-status personaggio
    lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
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
    schermo.blit(imgNumFrecce, (gsx // 32 * 1.2, gsy // 18 * 17))
    messaggio("x " + str(numFrecce), grigiochi, gsx // 32 * 1.8, gsy // 18 * 17.2, 40)
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 3, gsy // 18 * 17))
    if attp > 0:
        schermo.blit(attaccopiu, (gsx // 32 * 4, gsy // 18 * 17))
    if difp > 0:
        schermo.blit(difesapiu, (gsx // 32 * 5, gsy // 18 * 17))

    # disegno la vita del mostro / Colco / esca selezionato
    if nemicoInquadrato == "Colco":
        lungentot = int(((gpx * entot) / float(4)) // 15)
        lungen = int(((gpx * enrob) / float(4)) // 15)
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
        if surrisc > 0:
            schermo.blit(surriscaldato, (gpx + (gpx // 8), gpy // 4))
        if velp > 0:
            schermo.blit(velocitapiu, ((gpx * 2) + (gpx // 8), gpy // 4))
        if effp > 0:
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

    if not caricaTutto:
        pygame.display.update()


def attacca(x, y, npers, nrob, rx, ry, pers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, stanzaa, stanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, attVicino, attLontano, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, numFrecce, nemicoInquadrato):
    xp = x
    yp = y
    if nemicoInquadrato == "Colco":
        xp = rx
        yp = ry
    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
        xp = nemicoInquadrato.x
        yp = nemicoInquadrato.y
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vitaesca):
            if idEscaInquadrata == vitaesca[i]:
                xp = vitaesca[i + 2]
                yp = vitaesca[i + 3]
                break
            i += 4

    xvp = xp
    yvp = yp
    nxp = 0
    nyp = 0
    risposta = False
    difesa = 0

    puntat = puntatOut
    puntatogg = 0
    puntatogg1 = puntatDif
    puntatogg2 = puntatAtt
    puntatogg3 = puntatPor
    puntatogg4 = puntatSpinta
    puntatogg5 = puntatCof
    puntatogg6 = puntatArc

    # modifica puntatore a seconda dell'attacco
    if attacco == 1:
        puntatogg1 = puntatDif
        puntatogg2 = puntatAtt
        puntatogg3 = puntatPor
        puntatogg4 = puntatSpinta
        puntatogg5 = puntatCof
        puntatogg6 = puntatArc
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
    # disegno le caselle viste
    i = 0
    while i < len(caseviste):
        if caseviste[i + 2]:
            if ((caseviste[i] / gpx) + (caseviste[i + 1] / gpy)) % 2 == 0:
                schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
            if ((caseviste[i] / gpx) + (caseviste[i + 1] / gpy)) % 2 == 1:
                schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
        i += 3

    # vita-status personaggio
    lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
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
    schermo.blit(imgNumFrecce, (gsx // 32 * 1.2, gsy // 18 * 17))
    messaggio("x " + str(numFrecce), grigiochi, gsx // 32 * 1.8, gsy // 18 * 17.2, 40)
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 3, gsy // 18 * 17))
    if attp > 0:
        schermo.blit(attaccopiu, (gsx // 32 * 4, gsy // 18 * 17))
    if difp > 0:
        schermo.blit(difesapiu, (gsx // 32 * 5, gsy // 18 * 17))

    # controllo caselle attaccabili
    caseattactot = 0
    if attacco == 1:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, -1)
    if attacco == 2:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, gpx * 6)
    if attacco == 3:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, gpx * 5)
    if attacco == 4:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, gpx * 6)
    if attacco == 5:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, gpx * 5)
    if attacco == 6:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, gpx * 4)

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
    puntaPorta = False
    puntaCofanetto = False
    attaccato = False
    attaccoADistanza = False
    sposta = False
    while not risposta:
        if xp != xvp or yp != yvp:
            appenaCaricato = False
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

        if ((xvp / gpx) + (yvp / gpy)) % 2 == 0:
            schermo.blit(sfondinoa, (xvp, yvp))
        if ((xvp / gpx) + (yvp / gpy)) % 2 == 1:
            schermo.blit(sfondinob, (xvp, yvp))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # esci
                if event.key == pygame.K_q:
                    risposta = True
                    sposta = False
                    canaleSoundPuntatore.play(selind)
                # movimento puntatore
                tastop = event.key
                if event.key == pygame.K_e:
                    selezioneAvvenuta = False
                    if xp == rx and yp == ry:
                        selezioneAvvenuta = True
                        nemicoInquadrato = "Colco"
                    else:
                        i = 0
                        while i < len(vitaesca):
                            if xp == vitaesca[i + 2] and yp == vitaesca[i + 3]:
                                nemicoInquadrato = "Esca" + str(vitaesca[i])
                                selezioneAvvenuta = True
                            i += 4
                        if not selezioneAvvenuta:
                            for nemico in listaNemici:
                                if xp == nemico.x and yp == nemico.y:
                                    nemicoInquadrato = nemico
                                    selezioneAvvenuta = True
                    if not selezioneAvvenuta:
                        canaleSoundPuntatore.play(selimp)
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
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                        # apri/chiudi porta attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and suPorta:
                            apriChiudiPorta = [True, xp, yp]
                            sposta = True
                            risposta = True
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                        # apri cofanetto attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and suCofanetto:
                            apriCofanetto = [True, xp, yp]
                            sposta = True
                            risposta = True
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                        # attacco ravvicinato attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)):
                            infliggidanno = True
                            danno = attVicino
                            raggio = gpx * 0
                        # attacco lontano attacco = 1
                        elif attacco == 1 and not ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy) or (xp == x and yp == y) or (xp == rx and yp == ry)) and numFrecce > 0:
                            j = 0
                            while j < len(caseattactot):
                                if caseattactot[j] == xp and caseattactot[j + 1] == yp:
                                    if caseattactot[j + 2]:
                                        infliggidanno = True
                                        danno = attLontano
                                        raggio = gpx * 0
                                    break
                                j += 3
                        # difesa attacco = 1
                        elif attacco == 1 and (xp == x and yp == y):
                            difesa = 2
                            risposta = True
                        # bomba attacco = 2
                        if attacco == 2 and (abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6):
                            attaccato = True
                            # controllo caselle attaccabili
                            continua = True
                            # disegno le caselle attaccabili
                            i = 0
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
                            # disegno le caselle attaccabili
                            i = 0
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
                            # disegno le caselle attaccabili
                            i = 0
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                # conferma lancio esche
                                confesca = True
                                i = 0
                                while i < len(vettoreDenaro):
                                    if vettoreDenaro[i + 1] == xp and vettoreDenaro[i + 2] == yp:
                                        confesca = False
                                        break
                                    i += 3
                                i = 2
                                while i < len(vitaesca):
                                    if vitaesca[i] == xp and vitaesca[i + 1] == yp:
                                        confesca = False
                                        break
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
                            # disegno le caselle attaccabili
                            i = 0
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
                            # disegno le caselle attaccabili
                            i = 0
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

                        nemicoColpito = False
                        for nemico in listaNemici:
                            if (((abs(nemico.x - xp) <= raggio and abs(nemico.y - yp) <= raggio) and attacco != 1) or ((xp == nemico.x and yp == nemico.y) and attacco == 1)) and infliggidanno:
                                nemicoColpito = nemico
                                if statom == 1:
                                    nemico.avvelenato = True
                                if statom == 2:
                                    nemico.appiccicato = True
                                nemico.danneggia(danno, "Rallo")
                                # inquadro il nemico colpito se non sto usando un oggetto
                                if attacco == 1:
                                    nemicoInquadrato = nemico
                                sposta = True
                                risposta = True

                        # attacco da vicino
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and sposta and risposta and infliggidanno:
                            attaccato = True
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                        # attacco con arco
                        elif attacco == 1 and not ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and sposta and risposta and infliggidanno:
                            attaccato = True
                            attaccoADistanza = nemicoColpito
                            if abs(x - xp) > abs(y - yp):
                                if x < xp:
                                    npers = 1
                                if x > xp:
                                    npers = 2
                            if abs(y - yp) > abs(x - xp):
                                if y < yp:
                                    npers = 4
                                if y > yp:
                                    npers = 3
                            if (abs(x - xp) == abs(y - yp)) and (x != xp) and (y != yp):
                                c = random.randint(1, 2)
                                if x < xp and c == 1:
                                    npers = 1
                                if x > xp and c == 1:
                                    npers = 2
                                if y < yp and c == 2:
                                    npers = 4
                                if y > yp and c == 2:
                                    npers = 3

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
            # disegno le caselle viste
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2]:
                    if ((caseviste[i] / gpx) + (caseviste[i + 1] / gpy)) % 2 == 0:
                        schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                    if ((caseviste[i] / gpx) + (caseviste[i + 1] / gpy)) % 2 == 1:
                        schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                i += 3
            ricaricaschermo = False
            appenaCaricato = True

        # disegno le caselle attaccabili
        i = 0
        while i < len(caseattactot):
            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
            i = i + 3
        # visualizza campo attaccabile se sto usando un oggetto
        if attacco == 2:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (x - (gpx * 6), y - (gpy * 6)))
        if attacco == 3:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 11, gpy * 11))
            schermo.blit(campoattaccabile3, (x - (gpx * 5), y - (gpy * 5)))
        if attacco == 4:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (x - (gpx * 6), y - (gpy * 6)))
        if attacco == 5:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 11, gpy * 11))
            schermo.blit(campoattaccabile3, (x - (gpx * 5), y - (gpy * 5)))
        if attacco == 6:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 9, gpy * 9))
            schermo.blit(campoattaccabile3, (x - (gpx * 4), y - (gpy * 4)))

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

        # denaro: qta, x, y
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

        # robo
        schermo.blit(robot, (rx, ry))
        if surrisc > 0:
            schermo.blit(roboSurrisc, (rx, ry))
        schermo.blit(armrob, (rx, ry))
        # personaggio
        if not risposta:
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

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
            nemicoInCampoVisivoArco = False
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
                for nemico in listaNemici:
                    if xp == nemico.x and yp == nemico.y:
                        suPorta = False
                        suCofanetto = False
                        if (xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy):
                            puntatogg = puntatogg2
                        else:
                            puntatogg = puntatogg6
                            j = 0
                            while j < len(caseattactot):
                                if caseattactot[j] == nemico.x and caseattactot[j + 1] == nemico.y:
                                    if caseattactot[j + 2]:
                                        nemicoInCampoVisivoArco = True
                                    break
                                j += 3
                        break
            if (((xp == x and yp == y) or (xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and puntatogg != 0) or (puntatogg == puntatogg6 and nemicoInCampoVisivoArco and numFrecce > 0):
                puntat = puntatIn
            else:
                puntat = puntatOut
        if attacco == 2:
            if abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6:
                puntat = puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 3:
            if abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5:
                puntat = puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 4:
            if abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6:
                puntat = puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                        break
                    i = i + 3
                i = 0
                while i < len(vettoreDenaro):
                    if vettoreDenaro[i + 1] == xp and vettoreDenaro[i + 2] == yp:
                        puntat = puntatOut
                        break
                    i += 3
            else:
                puntat = puntatOut
        if attacco == 5:
            if abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5:
                puntat = puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = puntatOut
                    i = i + 3
            else:
                puntat = puntatOut
        if attacco == 6:
            if abs(x - xp) <= gpx * 4 and abs(y - yp) <= gpy * 4:
                puntat = puntatIn
                i = 0
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
            if ((xp / gpx) + (yp / gpy)) % 2 == 0:
                schermo.blit(sfondinoa, (xp, yp))
            if ((xp / gpx) + (yp / gpy)) % 2 == 1:
                schermo.blit(sfondinob, (xp, yp))

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

        # vita-status personaggio
        lungvitatot = int(((gpx * pvtot) / float(4)) // 5)
        lungvita = (lungvitatot * pv) // pvtot
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
        schermo.blit(imgNumFrecce, (gsx // 32 * 1.2, gsy // 18 * 17))
        messaggio("x " + str(numFrecce), grigiochi, gsx // 32 * 1.8, gsy // 18 * 17.2, 40)
        if avvele:
            schermo.blit(avvelenato, (gsx // 32 * 3, gsy // 18 * 17))
        if attp > 0:
            schermo.blit(attaccopiu, (gsx // 32 * 4, gsy // 18 * 17))
        if difp > 0:
            schermo.blit(difesapiu, (gsx // 32 * 5, gsy // 18 * 17))

        puntandoSuUnNemicoOColcoOEsca = False
        # disegna vita esche
        i = 0
        while i < len(vitaesca):
            if xp == vitaesca[i + 2] and yp == vitaesca[i + 3]:
                puntandoSuUnNemicoOColcoOEsca = True
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
                ricaricaschermo = True
            i += 4
        # disegna vita-status-raggio visivo nemici
        for nemico in listaNemici:
            if xp == nemico.x and yp == nemico.y:
                puntandoSuUnNemicoOColcoOEsca = True
                mx = nemico.x
                my = nemico.y
                pvm = nemico.vita
                pvmtot = nemico.vitaTotale
                raggiovista = nemico.raggioVisivo
                # controllo caselle attaccabili
                caseattactotMostri = trovacasattaccabili(mx, my, stanza, porte, cofanetti, nemico.raggioVisivo)
                # disegno le caselle attaccabili
                i = 0
                while i < len(caseattactotMostri):
                    if not caseattactotMostri[i + 2] and (caseattactotMostri[i] <= mx + raggiovista and caseattactotMostri[i + 1] <= my + raggiovista and caseattactotMostri[i] >= mx - raggiovista and caseattactotMostri[i + 1] >= my - raggiovista and not (caseattactotMostri[i] == mx and caseattactotMostri[i + 1] == my)):
                        schermo.blit(caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovista * 2) + gpx, (raggiovista * 2) + gpy))
                schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
                schermo.blit(sfondoMostro, (0, 0))
                if nemico.avvelenato:
                    schermo.blit(avvelenato, (gpx + (gpx // 8), gpy // 4))
                if nemico.appiccicato:
                    schermo.blit(appiccicoso, ((gpx * 2) + (gpx // 8), gpy // 4))
                schermo.blit(nemico.imgS, (0, 0))
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
                ricaricaschermo = True
                break
        # vita-status-campo visivo robo
        if xp == rx and yp == ry:
            puntandoSuUnNemicoOColcoOEsca = True
            if enrob > 0:
                # controllo caselle attaccabili
                raggiovista = gpx * 6
                caseattactotRobo = trovacasattaccabili(rx, ry, stanza, porte, cofanetti, raggiovista)
                # disegno le caselle attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        schermo.blit(caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(campoattaccabileRobo, ((raggiovista * 2) + gpx, (raggiovista * 2) + gpy))
                schermo.blit(campoattaccabile3, (rx - raggiovista, ry - raggiovista))
                ricaricaschermo = True
            lungentot = int(((gpx * entot) / float(4)) // 15)
            lungen = int(((gpx * enrob) / float(4)) // 15)
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
            if surrisc > 0:
                schermo.blit(surriscaldato, (gpx + (gpx // 8), gpy // 4))
            if velp > 0:
                schermo.blit(velocitapiu, ((gpx * 2) + (gpx // 8), gpy // 4))
            if effp > 0:
                schermo.blit(efficienzapiu, ((gpx * 3) + (gpx // 8), gpy // 4))
        # vita colco selezionato
        if nemicoInquadrato == "Colco" and not puntandoSuUnNemicoOColcoOEsca:
            if enrob > 0:
                # controllo caselle attaccabili
                raggiovista = gpx * 6
                caseattactotRobo = trovacasattaccabili(rx, ry, stanza, porte, cofanetti, raggiovista)
                # disegno le caselle attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        schermo.blit(caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(campoattaccabileRobo, ((raggiovista * 2) + gpx, (raggiovista * 2) + gpy))
                schermo.blit(campoattaccabile3, (rx - raggiovista, ry - raggiovista))
            lungentot = int(((gpx * entot) / float(4)) // 15)
            lungen = int(((gpx * enrob) / float(4)) // 15)
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
            if surrisc > 0:
                schermo.blit(surriscaldato, (gpx + (gpx // 8), gpy // 4))
            if velp > 0:
                schermo.blit(velocitapiu, ((gpx * 2) + (gpx // 8), gpy // 4))
            if effp > 0:
                schermo.blit(efficienzapiu, ((gpx * 3) + (gpx // 8), gpy // 4))
        # vita nemico selezionato
        elif not puntandoSuUnNemicoOColcoOEsca and not type(nemicoInquadrato) is str and nemicoInquadrato:
            mx = nemicoInquadrato.x
            my = nemicoInquadrato.y
            pvm = nemicoInquadrato.vita
            pvmtot = nemicoInquadrato.vitaTotale
            raggiovista = nemicoInquadrato.raggioVisivo
            # controllo caselle attaccabili
            caseattactotMostri = trovacasattaccabili(mx, my, stanza, porte, cofanetti, nemicoInquadrato.raggioVisivo)
            # disegno le caselle attaccabili
            i = 0
            while i < len(caseattactotMostri):
                if not caseattactotMostri[i + 2] and (
                        caseattactotMostri[i] <= mx + raggiovista and caseattactotMostri[i + 1] <= my + raggiovista and
                        caseattactotMostri[i] >= mx - raggiovista and caseattactotMostri[
                            i + 1] >= my - raggiovista and not (
                        caseattactotMostri[i] == mx and caseattactotMostri[i + 1] == my)):
                    schermo.blit(caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro,
                                                       ((raggiovista * 2) + gpx, (raggiovista * 2) + gpy))
            schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
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
        # vita esca selezionata
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and not puntandoSuUnNemicoOColcoOEsca:
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

        if not risposta:
            pygame.display.update()
        elif not sposta or not attaccato:
            attacco = 0
        pygame.event.pump()
        clockAttacco.tick(fpsInquadra)

    return sposta, creaesca, xp, yp, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco, attaccoADistanza, nemicoInquadrato
