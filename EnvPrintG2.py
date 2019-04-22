# -*- coding: utf-8 -*-

from GenericFuncG2 import *


def ambiente_movimento(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers,
                       stanzaa, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob, nemicoa, mxa, mya, mxav, myav, nemicob, mxb, myb, mxbv, mybv,
                       nemicoc, mxc, myc, mxcv, mycv, nemicod, mxd, myd, mxdv, mydv, nemicoe, mxe, mye, mxev, myev, nemicof, mxf, myf, mxfv, myfv,
                       nemicog, mxg, myg, mxgv, mygv, nemicoh, mxh, myh, mxhv, myhv, nemicoi, mxi, myi, mxiv, myiv, nemicol, mxl, myl, mxlv, mylv,
                       caricaini, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, numStanza):
    # sfondo
    if caricaini:
        schermo.blit(stanzaa, (0, 0))
        # porte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                vmurx = porte[i + 1]
                vmury = porte[i + 2]
                murx, mury, inutile, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, numStanza, False, False, False, False, porte, cofanetti)
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

    else:
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

    # disegnare casella sopra la vecchia posizione dei mostri
    j = 0
    while j < len(caseviste):
        if nemicoa != 0 and caseviste[j] == mxa and caseviste[j + 1] == mya and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxav == gpx * n:
                    m = 0
                    while m < 18:
                        if myav == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxav, myav))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxav, myav))
                        m = m + 1
                n = n + 1
        if nemicob != 0 and caseviste[j] == mxb and caseviste[j + 1] == myb and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxbv == gpx * n:
                    m = 0
                    while m < 18:
                        if mybv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxbv, mybv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxbv, mybv))
                        m = m + 1
                n = n + 1
        if nemicoc != 0 and caseviste[j] == mxc and caseviste[j + 1] == myc and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxcv == gpx * n:
                    m = 0
                    while m < 18:
                        if mycv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxcv, mycv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxcv, mycv))
                        m = m + 1
                n = n + 1
        if nemicod != 0 and caseviste[j] == mxd and caseviste[j + 1] == myd and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxdv == gpx * n:
                    m = 0
                    while m < 18:
                        if mydv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxdv, mydv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxdv, mydv))
                        m = m + 1
                n = n + 1
        if nemicoe != 0 and caseviste[j] == mxe and caseviste[j + 1] == mye and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxev == gpx * n:
                    m = 0
                    while m < 18:
                        if myev == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxev, myev))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxev, myev))
                        m = m + 1
                n = n + 1
        if nemicof != 0 and caseviste[j] == mxf and caseviste[j + 1] == myf and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxfv == gpx * n:
                    m = 0
                    while m < 18:
                        if myfv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxfv, myfv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxfv, myfv))
                        m = m + 1
                n = n + 1
        if nemicog != 0 and caseviste[j] == mxg and caseviste[j + 1] == myg and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxgv == gpx * n:
                    m = 0
                    while m < 18:
                        if mygv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxgv, mygv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxgv, mygv))
                        m = m + 1
                n = n + 1
        if nemicoh != 0 and caseviste[j] == mxh and caseviste[j + 1] == myh and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxhv == gpx * n:
                    m = 0
                    while m < 18:
                        if myhv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxhv, myhv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxhv, myhv))
                        m = m + 1
                n = n + 1
        if nemicoi != 0 and caseviste[j] == mxi and caseviste[j + 1] == myi and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxiv == gpx * n:
                    m = 0
                    while m < 18:
                        if myiv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxiv, myiv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxiv, myiv))
                        m = m + 1
                n = n + 1
        if nemicol != 0 and caseviste[j] == mxl and caseviste[j + 1] == myl and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxlv == gpx * n:
                    m = 0
                    while m < 18:
                        if mylv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxlv, mylv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxlv, mylv))
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
    schermo.blit(armrob, (rx, ry))

    # personaggio
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

    # vita-status personaggio
    lungvitatot = ((gpx * pvtot) / 4) // 5
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
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if attp > 0:
        schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
    if difp > 0:
        schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

    # vita-status robo
    lungentot = ((gpx * entot) / 4) // 10
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
        if nemicoa != 0 and caseviste[j] == mxa and caseviste[j + 1] == mya and caseviste[j + 2]:
            schermo.blit(nemicoa, (mxa, mya))
        if nemicob != 0 and caseviste[j] == mxb and caseviste[j + 1] == myb and caseviste[j + 2]:
            schermo.blit(nemicob, (mxb, myb))
        if nemicoc != 0 and caseviste[j] == mxc and caseviste[j + 1] == myc and caseviste[j + 2]:
            schermo.blit(nemicoc, (mxc, myc))
        if nemicod != 0 and caseviste[j] == mxd and caseviste[j + 1] == myd and caseviste[j + 2]:
            schermo.blit(nemicod, (mxd, myd))
        if nemicoe != 0 and caseviste[j] == mxe and caseviste[j + 1] == mye and caseviste[j + 2]:
            schermo.blit(nemicoe, (mxe, mye))
        if nemicof != 0 and caseviste[j] == mxf and caseviste[j + 1] == myf and caseviste[j + 2]:
            schermo.blit(nemicof, (mxf, myf))
        if nemicog != 0 and caseviste[j] == mxg and caseviste[j + 1] == myg and caseviste[j + 2]:
            schermo.blit(nemicog, (mxg, myg))
        if nemicoh != 0 and caseviste[j] == mxh and caseviste[j + 1] == myh and caseviste[j + 2]:
            schermo.blit(nemicoh, (mxh, myh))
        if nemicoi != 0 and caseviste[j] == mxi and caseviste[j + 1] == myi and caseviste[j + 2]:
            schermo.blit(nemicoi, (mxi, myi))
        if nemicol != 0 and caseviste[j] == mxl and caseviste[j + 1] == myl and caseviste[j + 2]:
            schermo.blit(nemicol, (mxl, myl))
        j = j + 3


def attacca(x, y, npers, nrob, rx, ry, pers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp,
            stanzaa, stanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob,
            nemicoa, mxa, mya, nemicob, mxb, myb, nemicoc, mxc, myc, nemicod, mxd, myd, nemicoe, mxe, mye,
            nemicof, mxf, myf, nemicog, mxg, myg, nemicoh, mxh, myh, nemicoi, mxi, myi, nemicol, mxl, myl,
            pvmatot, pvmbtot, pvmctot, pvmdtot, pvmetot, pvmftot, pvmgtot, pvmhtot, pvmitot, pvmltot,
            pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, statoma, statomb, statomc, statomd,
            statome, statomf, statomg, statomh, statomi, statoml, raggiovistaa, raggiovistab, raggiovistac,
            raggiovistad, raggiovistae, raggiovistaf, raggiovistag, raggiovistah, raggiovistai, raggiovistal,
            att, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob):
    if attacco <= 6:
        xp = x
        yp = y
    elif attacco > 6:
        xp = rx
        yp = ry
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
    if attacco == 7:
        puntatogg = pygame.image.load('Immagini\Oggetti\Scossa.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 8:
        puntatogg = pygame.image.load('Immagini\Oggetti\Frecciaelettrica.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 10:
        puntatogg = pygame.image.load('Immagini\Oggetti\Scossa+.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 11:
        puntatogg = pygame.image.load('Immagini\Oggetti\Frecciaelettrica+.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 13:
        puntatogg = pygame.image.load('Immagini\Oggetti\Scossa++.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 14:
        puntatogg = pygame.image.load('Immagini\Oggetti\Frecciaelettrica++.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 9 or attacco == 12 or attacco == 15:
        puntat = None
        puntatogg = None

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
            murx, mury, inutile, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, stanza, False, False, False, False, porte, cofanetti)
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
    lungvitatot = ((gpx * pvtot) / 4) // 5
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
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if attp > 0:
        schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
    if difp > 0:
        schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

    # vita-status robo
    lungentot = ((gpx * entot) / 4) // 10
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

    # tempeste elettriche
    if attacco == 9 or attacco == 12 or attacco == 15:
        infliggidanno = False
        if attacco == 9:
            infliggidanno = True
            raggio = gpx * 4
            danno = 3
        if attacco == 12:
            infliggidanno = True
            raggio = gpx * 5
            danno = 25
        if attacco == 15:
            infliggidanno = True
            raggio = gpx * 6
            danno = 50
        if (abs(mxa - rx) <= raggio and abs(mya - ry) <= raggio) and infliggidanno:
            pvma = pvma - danno
        if (abs(mxb - rx) <= raggio and abs(myb - ry) <= raggio) and infliggidanno:
            pvmb = pvmb - danno
        if (abs(mxc - rx) <= raggio and abs(myc - ry) <= raggio) and infliggidanno:
            pvmc = pvmc - danno
        if (abs(mxd - rx) <= raggio and abs(myd - ry) <= raggio) and infliggidanno:
            pvmd = pvmd - danno
        if (abs(mxe - rx) <= raggio and abs(mye - ry) <= raggio) and infliggidanno:
            pvme = pvme - danno
        if (abs(mxf - rx) <= raggio and abs(myf - ry) <= raggio) and infliggidanno:
            pvmf = pvmf - danno
        if (abs(mxg - rx) <= raggio and abs(myg - ry) <= raggio) and infliggidanno:
            pvmg = pvmg - danno
        if (abs(mxh - rx) <= raggio and abs(myh - ry) <= raggio) and infliggidanno:
            pvmh = pvmh - danno
        if (abs(mxi - rx) <= raggio and abs(myi - ry) <= raggio) and infliggidanno:
            pvmi = pvmi - danno
        if (abs(mxl - rx) <= raggio and abs(myl - ry) <= raggio) and infliggidanno:
            pvml = pvml - danno
        risposta = True
        sposta = True

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
                    selind.play()
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
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and suPorta:
                            apriChiudiPorta = [True, xp, yp]
                            sposta = True
                            risposta = True
                        # apri cofanetto attacco = 1
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and suCofanetto:
                            apriCofanetto = [True, xp, yp]
                            sposta = True
                            risposta = True
                        # normale attacco = 1
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)):
                            infliggidanno = True
                            danno = att
                            raggio = gpx * 0
                        # difesa attacco = 1
                        elif attacco == 1 and (xp == x and yp == y):
                            difesa = 2
                            risposta = True
                        # bomba attacco = 2
                        if attacco == 2 and (abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6):
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
                                if (xp == mxa and yp == mya) or (xp == mxb and yp == myb) or (xp == mxc and yp == myc) or (xp == mxd and yp == myd) or (xp == mxe and yp == mye) or (xp == mxf and yp == myf) or (xp == mxg and yp == myg) or (xp == mxh and yp == myh) or (xp == mxi and yp == myi) or (xp == mxl and yp == myl):
                                    confesca = False
                                if confesca:
                                    infliggidanno = True
                                    danno = 0
                                    raggio = 0
                                    creaesca = True
                                    sposta = True
                                    risposta = True
                                else:
                                    selimp.play()
                        # bomba appiccicosa attacco = 5
                        if attacco == 5 and (abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5):
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
                        # scossa attacco = 7
                        if attacco == 7 and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)):
                            infliggidanno = True
                            danno = 10
                            raggio = gpx * 0
                        # freccia elettrica attacco = 8
                        if attacco == 8 and (abs(rx - xp) <= gpx * 6 and abs(ry - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 5
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # scossa+ attacco = 10
                        if attacco == 10 and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)):
                            infliggidanno = True
                            danno = 100
                            raggio = gpx * 0
                        # freccia elettrica+ attacco = 11
                        if attacco == 11 and (abs(rx - xp) <= gpx * 6 and abs(ry - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 50
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # scossa++ attacco = 13
                        if attacco == 13 and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)):
                            infliggidanno = True
                            danno = 200
                            raggio = gpx * 0
                        # freccia elettrica++ attacco = 14
                        if attacco == 14 and (abs(rx - xp) <= gpx * 6 and abs(ry - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 100
                                raggio = gpx * 0
                                sposta = True
                                risposta = True

                        if (((abs(mxa - xp) <= raggio and abs(mya - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxa and yp == mya) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statoma == 2:
                                    statoma = 3
                                else:
                                    statoma = 1
                            if statom == 2:
                                if statoma == 1:
                                    statoma = 3
                                else:
                                    statoma = 2
                            pvma = pvma - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxb - xp) <= raggio and abs(myb - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxb and yp == myb) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomb == 2:
                                    statomb = 3
                                else:
                                    statomb = 1
                            if statom == 2:
                                if statomb == 1:
                                    statomb = 3
                                else:
                                    statomb = 2
                            pvmb = pvmb - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxc - xp) <= raggio and abs(myc - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxc and yp == myc) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomc == 2:
                                    statomc = 3
                                else:
                                    statomc = 1
                            if statom == 2:
                                if statomc == 1:
                                    statomc = 3
                                else:
                                    statomc = 2
                            pvmc = pvmc - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxd - xp) <= raggio and abs(myd - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxd and yp == myd) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomd == 2:
                                    statomd = 3
                                else:
                                    statomd = 1
                            if statom == 2:
                                if statomd == 1:
                                    statomd = 3
                                else:
                                    statomd = 2
                            pvmd = pvmd - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxe - xp) <= raggio and abs(mye - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxe and yp == mye) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statome == 2:
                                    statome = 3
                                else:
                                    statome = 1
                            if statom == 2:
                                if statome == 1:
                                    statome = 3
                                else:
                                    statome = 2
                            pvme = pvme - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxf - xp) <= raggio and abs(myf - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxf and yp == myf) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomf == 2:
                                    statomf = 3
                                else:
                                    statomf = 1
                            if statom == 2:
                                if statomf == 1:
                                    statomf = 3
                                else:
                                    statomf = 2
                            pvmf = pvmf - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxg - xp) <= raggio and abs(myg - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxg and yp == myg) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomg == 2:
                                    statomg = 3
                                else:
                                    statomg = 1
                            if statom == 2:
                                if statomg == 1:
                                    statomg = 3
                                else:
                                    statomg = 2
                            pvmg = pvmg - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxh - xp) <= raggio and abs(myh - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxh and yp == myh) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomh == 2:
                                    statomh = 3
                                else:
                                    statomh = 1
                            if statom == 2:
                                if statomh == 1:
                                    statomh = 3
                                else:
                                    statomh = 2
                            pvmh = pvmh - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxi - xp) <= raggio and abs(myi - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxi and yp == myi) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomi == 2:
                                    statomi = 3
                                else:
                                    statomi = 1
                            if statom == 2:
                                if statomi == 1:
                                    statomi = 3
                                else:
                                    statomi = 2
                            pvmi = pvmi - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxl - xp) <= raggio and abs(myl - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxl and yp == myl) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statoml == 2:
                                    statoml = 3
                                else:
                                    statoml = 1
                            if statom == 2:
                                if statoml == 1:
                                    statoml = 3
                                else:
                                    statoml = 2
                            pvml = pvml - danno
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
                            rumoreattacco.play()
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
                        # scossa se c'e' il mostro
                        if (attacco == 7 or attacco == 10 or attacco == 13) and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)) and sposta and risposta:
                            if xp == rx + gpx and yp == ry:
                                nrob = 1
                            if xp == rx - gpx and yp == ry:
                                nrob = 2
                            if xp == rx and yp == ry + gpy:
                                nrob = 3
                            if xp == rx and yp == ry - gpy:
                                nrob = 4
                            rumoreattacco.play()
                        # scossa se non c'e' il mostro
                        elif (attacco == 7 or attacco == 10 or attacco == 13) and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)) and not sposta and not risposta:
                            if xp == rx + gpx and yp == ry:
                                nrob = 1
                            if xp == rx - gpx and yp == ry:
                                nrob = 2
                            if xp == rx and yp == ry + gpy:
                                nrob = 3
                            if xp == rx and yp == ry - gpy:
                                nrob = 4
                            rumoreattacco.play()
                            sposta = True
                            risposta = True

                        if not risposta:
                            selimp.play()
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
                    murx, mury, inutile, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, stanza, False,
                                                                                False, False, False, porte, cofanetti)
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

        # visualizza campo attaccabile
        if attacco == 1:
            schermo.blit(campoattaccabile1, (x - gpx, y - gpy))
            # controllo caselle attaccabili
            caseattactot = [x + gpx, y, True, x - gpx, y, True, x, y + gpy, True, x, y - gpy, True]
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[2] = False
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[5] = False
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[8] = False
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[11] = False
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
        if attacco == 7 or attacco == 10 or attacco == 13:
            schermo.blit(campoattaccabile1, (rx - gpx, ry - gpy))
            # controllo caselle attaccabili
            caseattactot = [rx + gpx, ry, True, rx - gpx, ry, True, rx, ry + gpy, True, rx, ry - gpy, True]
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[2] = False
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[5] = False
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[8] = False
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True ,False, porte, cofanetti)
            if nmury == mury:
                caseattactot[11] = False
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2]:
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 8 or attacco == 11 or attacco == 14:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (rx - (gpx * 6), ry - (gpy * 6)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= rx + gpx * 6 and caseattactot[i + 1] <= ry + gpy * 6 and caseattactot[i] >= rx - gpx * 6 and caseattactot[i + 1] >= ry - gpy * 6 and not (caseattactot[i] == rx and caseattactot[i + 1] == ry)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3

        # mettere il puntatore su porte
        i = 0
        while i < len(porte):
            if porte[i + 1] == xp + nxp and porte[i + 2] == yp + nyp and not porte[i + 3]:
                puntaPorta = True
                xp = xp + nxp
                yp = yp + nyp
            i = i + 4
        # mettere il puntatore su cofanetti
        puntaCofanetto = False
        i = 0
        while i < len(cofanetti):
            if cofanetti[i + 1] == xp + nxp and cofanetti[i + 2] == yp + nyp:
                puntaCofanetto = True
                xp = xp + nxp
                yp = yp + nyp
            i = i + 4
        # movimento inquadra (ultimi 4 inutili)
        if not puntaPorta and not puntaCofanetto:
            xp, yp, stanza, carim, muovi, cambiosta = muri_porte(xp, yp, nxp, nyp, stanza, False, 0, True, False, porte, cofanetti)
        # movimento inquadra quando si è sulle porte
        if puntaPorta:
            i = 0
            while i < len(caseviste):
                if caseviste[i] == xp + nxp and caseviste[i + 1] == yp + nyp:
                    if caseviste[i + 2]:
                        xp = xp + nxp
                        yp = yp + nyp
                        puntaPorta = False
                i = i + 3

        # esche: id, vita, xesca, yesca
        i = 0
        while i < len(vitaesca):
            schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
            i = i + 4

        # robo
        schermo.blit(robot, (rx, ry))
        schermo.blit(armrob, (rx, ry))
        # personaggio
        if not risposta:
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

        # disegnare i mostri
        j = 0
        while j < len(caseviste):
            if nemicoa != 0 and caseviste[j] == mxa and caseviste[j + 1] == mya and caseviste[j + 2]:
                schermo.blit(nemicoa, (mxa, mya))
            if nemicob != 0 and caseviste[j] == mxb and caseviste[j + 1] == myb and caseviste[j + 2]:
                schermo.blit(nemicob, (mxb, myb))
            if nemicoc != 0 and caseviste[j] == mxc and caseviste[j + 1] == myc and caseviste[j + 2]:
                schermo.blit(nemicoc, (mxc, myc))
            if nemicod != 0 and caseviste[j] == mxd and caseviste[j + 1] == myd and caseviste[j + 2]:
                schermo.blit(nemicod, (mxd, myd))
            if nemicoe != 0 and caseviste[j] == mxe and caseviste[j + 1] == mye and caseviste[j + 2]:
                schermo.blit(nemicoe, (mxe, mye))
            if nemicof != 0 and caseviste[j] == mxf and caseviste[j + 1] == myf and caseviste[j + 2]:
                schermo.blit(nemicof, (mxf, myf))
            if nemicog != 0 and caseviste[j] == mxg and caseviste[j + 1] == myg and caseviste[j + 2]:
                schermo.blit(nemicog, (mxg, myg))
            if nemicoh != 0 and caseviste[j] == mxh and caseviste[j + 1] == myh and caseviste[j + 2]:
                schermo.blit(nemicoh, (mxh, myh))
            if nemicoi != 0 and caseviste[j] == mxi and caseviste[j + 1] == myi and caseviste[j + 2]:
                schermo.blit(nemicoi, (mxi, myi))
            if nemicol != 0 and caseviste[j] == mxl and caseviste[j + 1] == myl and caseviste[j + 2]:
                schermo.blit(nemicol, (mxl, myl))
            j = j + 3

        # porte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                vmurx = porte[i + 1]
                vmury = porte[i + 2]
                murx, mury, inutile, inutile, inutile, inutile = muri_porte(vmurx, vmury, gpx, 0, stanza, False,
                                                                            False, False, False, porte, cofanetti)
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
                if not suPorta and not suCofanetto and ((xp == mxa and yp == mya and nemicoa != 0) or (xp == mxb and yp == myb and nemicob != 0) or (xp == mxc and yp == myc and nemicoc != 0) or (xp == mxd and yp == myd and nemicod != 0) or (xp == mxe and yp == mye and nemicoe != 0) or (xp == mxf and yp == myf and nemicof != 0) or (xp == mxg and yp == myg and nemicog != 0) or (xp == mxh and yp == myh and nemicoh != 0) or (xp == mxi and yp == myi and nemicoi != 0) or (xp == mxl and yp == myl and nemicol != 0)):
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
        listaNemici = [mxa, mya, statoma, nemicoa, pvma, pvmatot, raggiovistaa, mxb, myb, statomb, nemicob, pvmb, pvmbtot, raggiovistab, mxc, myc, statomc, nemicoc, pvmc, pvmctot, raggiovistac, mxd, myd, statomd, nemicod, pvmd, pvmdtot, raggiovistad, mxe, mye, statome, nemicoe, pvme, pvmetot, raggiovistae, mxf, myf, statomf, nemicof, pvmf, pvmftot, raggiovistaf, mxg, myg, statomg, nemicog, pvmg, pvmgtot, raggiovistag, mxh, myh, statomh, nemicoh, pvmh, pvmhtot, raggiovistah, mxi, myi, statomi, nemicoi, pvmi, pvmitot, raggiovistai, mxl, myl, statoml, nemicol, pvml, pvmltot, raggiovistal]
        j = 0
        while j < len(listaNemici):
            mx = listaNemici[j]
            my = listaNemici[j + 1]
            statom = listaNemici[j + 2]
            nemico = listaNemici[j + 3]
            pvm = listaNemici[j + 4]
            pvmtot = listaNemici[j + 5]
            raggiovista = listaNemici[j + 6]
            if xp == mx and yp == my and nemico != 0:
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
                if statom == 1 or statom == 3:
                    schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
                if statom == 2 or statom == 3:
                    schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
                schermo.blit(nemico, (gsx // 32 * 1, gpy // 3))
                fineindvitamost = pygame.transform.scale(fineindvita, (gpx // 12, gpy // 4))
                if pvmtot > 1500:
                    indvitamost = pygame.transform.scale(indvita, (((gpx * 1500) / 4) // 15, gpy // 4))
                    schermo.blit(fineindvitamost, ((gsx // 32 * 2) + 1500, gpy // 3))
                    if pvm > 15000:
                        pvm = 1500
                        vitanemsucc = pygame.transform.scale(vitanemico00, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico9
                    elif pvm > 13500:
                        pvm -= 13500
                        vitanemsucc = pygame.transform.scale(vitanemico8, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico9
                    elif pvm > 12000:
                        pvm -= 12000
                        vitanemsucc = pygame.transform.scale(vitanemico7, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico8
                    elif pvm > 10500:
                        pvm -= 10500
                        vitanemsucc = pygame.transform.scale(vitanemico6, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico7
                    elif pvm > 9000:
                        pvm -= 9000
                        vitanemsucc = pygame.transform.scale(vitanemico5, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico6
                    elif pvm > 7500:
                        pvm -= 7500
                        vitanemsucc = pygame.transform.scale(vitanemico4, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico5
                    elif pvm > 6000:
                        pvm -= 6000
                        vitanemsucc = pygame.transform.scale(vitanemico3, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico4
                    elif pvm > 4500:
                        pvm -= 4500
                        vitanemsucc = pygame.transform.scale(vitanemico2, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico3
                    elif pvm > 3000:
                        pvm -= 3000
                        vitanemsucc = pygame.transform.scale(vitanemico1, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico2
                    elif pvm > 1500:
                        pvm -= 1500
                        vitanemsucc = pygame.transform.scale(vitanemico0, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico1
                    else:
                        vitanemsucc = pygame.transform.scale(vitanemico00, (((gpx * 1500) / 4) // 15, gpy // 4))
                        vitanemico = vitanemico0
                else:
                    lungvitatot = ((gpx * pvmtot) / 4) // 15
                    indvitamost = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
                    schermo.blit(fineindvitamost, ((gsx // 32 * 2) + lungvitatot, gpy // 3))
                    vitanemsucc = pygame.transform.scale(vitanemico00, ((gpx // 4) * (lungvitatot // 15), gpy // 4))
                    vitanemico = vitanemico0
                lungvita = ((gpx * pvm) / 4) // 15
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
        if not ((xp == mxa and yp == mya and nemicoa != 0) or (xp == mxb and yp == myb and nemicob != 0) or (xp == mxc and yp == myc and nemicoc != 0) or (xp == mxd and yp == myd and nemicod != 0) or (xp == mxe and yp == mye and nemicoe != 0) or (xp == mxf and yp == myf and nemicof != 0) or (xp == mxg and yp == myg and nemicog != 0) or (xp == mxh and yp == myh and nemicoh != 0) or (xp == mxi and yp == myi and nemicoi != 0) or (xp == mxl and yp == myl and nemicol != 0)):
            ricaricaschermo = False
            if (xvp == mxa and yvp == mya and nemicoa != 0) or (xvp == mxb and yvp == myb and nemicob != 0) or (xvp == mxc and yvp == myc and nemicoc != 0) or (xvp == mxd and yvp == myd and nemicod != 0) or (xvp == mxe and yvp == mye and nemicoe != 0) or (xvp == mxf and yvp == myf and nemicof != 0) or (xvp == mxg and yvp == myg and nemicog != 0) or (xvp == mxh and yvp == myh and nemicoh != 0) or (xvp == mxi and yvp == myi and nemicoi != 0) or (xvp == mxl and yvp == myl and nemicol != 0):
                ricaricaschermo = True
                appenaCaricato = False

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
        lungvitatot = ((gpx * pvtot) / 4) // 5
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
        schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
        if avvele:
            schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
        if attp > 0:
            schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
        if difp > 0:
            schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

        # vita-status robo
        lungentot = ((gpx * entot) / 4) // 10
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

        if not risposta:
            pygame.display.update()
        clock.tick(fpsmenu)

    return pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, sposta, creaesca, xp, yp, statoma, statomb, statomc, statomd, statome, statomf, statomg, statomh, statomi, statoml, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco
