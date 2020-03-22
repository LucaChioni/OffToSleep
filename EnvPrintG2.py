# -*- coding: utf-8 -*-

from GenericFuncG2 import *
from FadeToBlackClass import *


def disegnaAmbiente(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, numStanza, listaNemici, caricaTutto, vettoreDenaro, numFrecce, nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, eschePrimaDelTurno, listaPersonaggi, primaDiAnima, stanzaCambiata, uscitoDaMenu):
    if caricaTutto:
        GlobalVarG2.schermo.blit(imgSfondoStanza, (0, 0))
        # porte
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
        # cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - GlobalVarG2.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                        caseviste[j] == cofanetti[i + 1] + GlobalVarG2.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVarG2.gpy) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVarG2.gpy)) and \
                        caseviste[j + 2]:
                    GlobalVarG2.schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                    if cofanetti[i + 3]:
                        GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                    break
                j = j + 3
            i = i + 4
        # disegno le caselle viste
        i = 0
        while i < len(caseviste):
            if caseviste[i + 2]:
                if ((caseviste[i] / GlobalVarG2.gpx) + (caseviste[i + 1] / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                if ((caseviste[i] / GlobalVarG2.gpx) + (caseviste[i + 1] / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
            i += 3

    # disegnare casella sopra la vecchia posizione dei personaggi e mostri
    if ((vx / GlobalVarG2.gpx) + (vy / GlobalVarG2.gpy)) % 2 == 0:
        GlobalVarG2.schermo.blit(sfondinoa, (vx, vy))
    if ((vx / GlobalVarG2.gpx) + (vy / GlobalVarG2.gpy)) % 2 == 1:
        GlobalVarG2.schermo.blit(sfondinob, (vx, vy))
    if ((vrx / GlobalVarG2.gpx) + (vry / GlobalVarG2.gpy)) % 2 == 0:
        GlobalVarG2.schermo.blit(sfondinoa, (vrx, vry))
    if ((vrx / GlobalVarG2.gpx) + (vry / GlobalVarG2.gpy)) % 2 == 1:
        GlobalVarG2.schermo.blit(sfondinob, (vrx, vry))
    j = 0
    while j < len(caseviste):
        for nemico in listaNemici:
            if caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                if ((nemico.vx / GlobalVarG2.gpx) + (nemico.vy / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (nemico.vx, nemico.vy))
                if ((nemico.vx / GlobalVarG2.gpx) + (nemico.vy / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (nemico.vx, nemico.vy))
        j += 3

    # backbround occhio/chiave
    GlobalVarG2.schermo.blit(GlobalVarG2.sfochiaveocchio, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 5), 0))

    # vista nemici
    if apriocchio:
        GlobalVarG2.schermo.blit(GlobalVarG2.occhioape, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))
    else:
        GlobalVarG2.schermo.blit(GlobalVarG2.occhiochiu, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))

    # chiave robo
    if chiamarob:
        GlobalVarG2.schermo.blit(GlobalVarG2.chiaveroboacc, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))
    else:
        GlobalVarG2.schermo.blit(GlobalVarG2.chiaverobospe, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))

    # GlobalVarG2.esche: id, vita, xesca, yesca
    i = 0
    while i < len(vitaesca):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and caseviste[j + 2]:
                if primaDiAnima:
                    k = 0
                    while k < len(eschePrimaDelTurno):
                        if eschePrimaDelTurno[k] == vitaesca[i]:
                            if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 0:
                                GlobalVarG2.schermo.blit(sfondinoa, (vitaesca[i + 2], vitaesca[i + 3]))
                            if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 1:
                                GlobalVarG2.schermo.blit(sfondinob, (vitaesca[i + 2], vitaesca[i + 3]))
                            GlobalVarG2.schermo.blit(GlobalVarG2.esche, (vitaesca[i + 2], vitaesca[i + 3]))
                            break
                        k += 1
                else:
                    if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 0:
                        GlobalVarG2.schermo.blit(sfondinoa, (vitaesca[i + 2], vitaesca[i + 3]))
                    if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 1:
                        GlobalVarG2.schermo.blit(sfondinob, (vitaesca[i + 2], vitaesca[i + 3]))
                    GlobalVarG2.schermo.blit(GlobalVarG2.esche, (vitaesca[i + 2], vitaesca[i + 3]))
                break
            j += 3
        i += 4

    # denaro: qta, x, y
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

    # robo (anche in caso di raffreddamento e autoricarica)
    if (raffreddamento and not primaDiAnima) or (raffredda > 0 and not raffreddamento):
        GlobalVarG2.schermo.blit(armrobS, (rx, ry))
        GlobalVarG2.schermo.blit(GlobalVarG2.robos, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVarG2.vetAnimazioniTecniche):
            if GlobalVarG2.vetAnimazioniTecniche[i] == "raffred":
                imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
    elif (ricarica1 and not primaDiAnima) or (autoRic1 > 0 and not ricarica1):
        GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVarG2.vetAnimazioniTecniche):
            if GlobalVarG2.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
    elif (ricarica2 and not primaDiAnima) or (autoRic2 > 0 and not ricarica2):
        GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVarG2.vetAnimazioniTecniche):
            if GlobalVarG2.vetAnimazioniTecniche[i] == "ricarica+":
                imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
    else:
        GlobalVarG2.schermo.blit(robot, (rx, ry))
        if surrisc > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx, ry))
        GlobalVarG2.schermo.blit(armrob, (rx, ry))

    disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

    # disegno tutti i personaggi
    for personaggio in listaPersonaggi:
        j = 0
        while j < len(caseviste):
            if caseviste[j] == personaggio.x and caseviste[j + 1] == personaggio.y and caseviste[j + 2]:
                if ((personaggio.x / GlobalVarG2.gpx) + (personaggio.y / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (personaggio.x, personaggio.y))
                if ((personaggio.x / GlobalVarG2.gpx) + (personaggio.y / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (personaggio.x, personaggio.y))
                GlobalVarG2.schermo.blit(personaggio.imgAttuale, (personaggio.x, personaggio.y))
                break
            j += 3

    # vita-status rallo
    lungvitatot = int(((GlobalVarG2.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
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
    messaggio("x " + str(numFrecce), GlobalVarG2.grigiochi, int(GlobalVarG2.gsx // 32 * 1.8), int(GlobalVarG2.gsy // 18 * 17.2), 40)
    if avvele:
        GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gsx // 32 * 3, GlobalVarG2.gsy // 18 * 17))
    if attp > 0:
        GlobalVarG2.schermo.blit(GlobalVarG2.attaccopiu, (GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 17))
    if difp > 0:
        GlobalVarG2.schermo.blit(GlobalVarG2.difesapiu, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 17))

    # disegno la vita del mostro / Colco / esca selezionato
    if nemicoInquadrato == "Colco" or not nemicoInquadrato:
        lungentot = int(((GlobalVarG2.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalVarG2.gpx * enrob) / float(4)) // 15)
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
        if surrisc > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.surriscaldato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
        if velp > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.velocitapiu, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
        if effp > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.efficienzapiu, ((GlobalVarG2.gpx * 3) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vitaesca):
            if idEscaInquadrata == vitaesca[i]:
                pvEsca = vitaesca[i + 1]
                if primaDiAnima:
                    idEscaInizioturno = 0
                    j = 0
                    while j < len(statoEscheInizioTurno):
                        if statoEscheInizioTurno[j] == nemicoInquadrato:
                            idEscaInizioturno = j
                            break
                        j += 2
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
                GlobalVarG2.schermo.blit(fineindvitamost, (GlobalVarG2.gpx + int(((GlobalVarG2.gpx * 1000) / float(4)) // 15), 0))
                GlobalVarG2.schermo.blit(vitaesche, (GlobalVarG2.gpx, 0))
                break
            i += 4
    elif nemicoInquadrato and not type(nemicoInquadrato) is str:
        pvm = nemicoInquadrato.vita
        nemicoAvvelenato = nemicoInquadrato.avvelenato
        nemicoAppiccicato = nemicoInquadrato.appiccicato
        if primaDiAnima:
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

    # disegnare i mostri
    j = 0
    while j < len(caseviste):
        for nemico in listaNemici:
            if not nemico.morto and caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                GlobalVarG2.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                if nemico.appiccicato:
                    GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                if nemico.avvelenato:
                    GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
        j = j + 3

    # disegno img GlobalVarG2.puntatoreInquadraNemici
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

    if not caricaTutto:
        if stanzaCambiata or uscitoDaMenu > 0:
            if uscitoDaMenu > 0:
                sprites = pygame.sprite.Group(Fade(1))
            else:
                sprites = pygame.sprite.Group(Fade(2))
            schermoFadeToBlack = GlobalVarG2.schermo.copy()
            i = 0
            while i <= 6:
                sprites.update()
                GlobalVarG2.schermo.blit(schermoFadeToBlack, (0, 0))
                sprites.draw(GlobalVarG2.schermo)
                pygame.display.update()
                GlobalVarG2.clockFadeToBlack.tick(GlobalVarG2.fpsFadeToBlack)
                i += 1
        else:
            pygame.display.update()


def attacca(x, y, npers, nrob, rx, ry, pers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, stanzaa, stanza, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, attVicino, attLontano, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, numFrecce, nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf):
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

    attaccoDiRallo = [False, 0, False]
    xvp = xp
    yvp = yp
    nxp = 0
    nyp = 0
    risposta = False
    difesa = 0

    puntat = GlobalVarG2.puntatOut
    puntatogg = 0
    puntatogg1 = GlobalVarG2.puntatDif
    puntatogg2 = GlobalVarG2.puntatAtt
    puntatogg3 = GlobalVarG2.puntatPor
    puntatogg4 = GlobalVarG2.puntatSpinta
    puntatogg5 = GlobalVarG2.puntatCof
    puntatogg6 = GlobalVarG2.puntatArc
    puntatogg7 = GlobalVarG2.puntatDialoghi

    # modifica puntatore a seconda dell'attacco
    if attacco == 1:
        puntatogg1 = GlobalVarG2.puntatDif
        puntatogg2 = GlobalVarG2.puntatAtt
        puntatogg3 = GlobalVarG2.puntatPor
        puntatogg4 = GlobalVarG2.puntatSpinta
        puntatogg5 = GlobalVarG2.puntatCof
        puntatogg6 = GlobalVarG2.puntatArc
        puntatogg7 = GlobalVarG2.puntatDialoghi
    if attacco == 2:
        puntatogg = GlobalVarG2.puntatBom
    if attacco == 3:
        puntatogg = GlobalVarG2.puntatBoV
    if attacco == 4:
        puntatogg = GlobalVarG2.puntatEsc
    if attacco == 5:
        puntatogg = GlobalVarG2.puntatBoA
    if attacco == 6:
        puntatogg = GlobalVarG2.puntatBoP

    GlobalVarG2.schermo.blit(stanzaa, (0, 0))
    # backbround occhio/chiave
    GlobalVarG2.schermo.blit(GlobalVarG2.sfochiaveocchio, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 5), 0))

    # vista nemici
    if apriocchio:
        GlobalVarG2.schermo.blit(GlobalVarG2.occhioape, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))
    else:
        GlobalVarG2.schermo.blit(GlobalVarG2.occhiochiu, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))

    # chiave robo
    if chiamarob:
        GlobalVarG2.schermo.blit(GlobalVarG2.chiaveroboacc, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))
    else:
        GlobalVarG2.schermo.blit(GlobalVarG2.chiaverobospe, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))
    # porte
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            vmurx = porte[i + 1]
            vmury = porte[i + 2]
            murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, GlobalVarG2.gpx, 0, stanza, False, False, False, porte, cofanetti)
            GlobalVarG2.schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
            if vmurx == murx and vmury == mury:
                GlobalVarG2.schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
            else:
                GlobalVarG2.schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
        i = i + 4
    # cofanetti
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
            j = j + 3
        i = i + 4
    # disegno le caselle viste
    i = 0
    while i < len(caseviste):
        if caseviste[i + 2]:
            if ((caseviste[i] / GlobalVarG2.gpx) + (caseviste[i + 1] / GlobalVarG2.gpy)) % 2 == 0:
                GlobalVarG2.schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
            if ((caseviste[i] / GlobalVarG2.gpx) + (caseviste[i + 1] / GlobalVarG2.gpy)) % 2 == 1:
                GlobalVarG2.schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
        i += 3

    # vita-status personaggio
    lungvitatot = int(((GlobalVarG2.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
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
    GlobalVarG2.schermo.blit(GlobalVarG2.imgNumFrecce, (GlobalVarG2.gsx // 32 * 1.2, GlobalVarG2.gsy // 18 * 17))
    messaggio("x " + str(numFrecce), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1.8, GlobalVarG2.gsy // 18 * 17.2, 40)
    if avvele:
        GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gsx // 32 * 3, GlobalVarG2.gsy // 18 * 17))
    if attp > 0:
        GlobalVarG2.schermo.blit(GlobalVarG2.attaccopiu, (GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 17))
    if difp > 0:
        GlobalVarG2.schermo.blit(GlobalVarG2.difesapiu, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 17))

    # controllo caselle attaccabili
    raggioDiLancio = 0
    caseattactot = 0
    if attacco == 1:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, -1)
    if attacco == 2:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, GlobalVarG2.gpx * 6)
        raggioDiLancio = 6
    if attacco == 3:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, GlobalVarG2.gpx * 5)
        raggioDiLancio = 5
    if attacco == 4:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, GlobalVarG2.gpx * 6)
        raggioDiLancio = 6
    if attacco == 5:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, GlobalVarG2.gpx * 5)
        raggioDiLancio = 5
    if attacco == 6:
        caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti, GlobalVarG2.gpx * 4)
        raggioDiLancio = 4

    listaNemiciVisti = []
    for nemico in listaNemici:
        if nemico.inCasellaVista:
            listaNemiciVisti.append(nemico)

    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    tastotempfps = 2
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
    interagisciConPersonaggio = False
    attaccoConfermato = False
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
                nyp = -GlobalVarG2.gpy
            if tastop == pygame.K_a:
                nxp = -GlobalVarG2.gpx
            if tastop == pygame.K_s:
                nyp = GlobalVarG2.gpy
            if tastop == pygame.K_d:
                nxp = GlobalVarG2.gpx
            tastotempfps = 2
            xvp = xp
            yvp = yp

        if ((xvp / GlobalVarG2.gpx) + (yvp / GlobalVarG2.gpy)) % 2 == 0:
            GlobalVarG2.schermo.blit(sfondinoa, (xvp, yvp))
        if ((xvp / GlobalVarG2.gpx) + (yvp / GlobalVarG2.gpy)) % 2 == 1:
            GlobalVarG2.schermo.blit(sfondinob, (xvp, yvp))

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if deltaXMouse != 0 or deltaYMouse != 0:
            if not GlobalVarG2.mouseVisibile:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            casellaTrovata = False
            i = 0
            while i < len(caseviste):
                if caseviste[i] < xMouse < caseviste[i] + GlobalVarG2.gpx and caseviste[i + 1] < yMouse < caseviste[i + 1] + GlobalVarG2.gpy and caseviste[i + 2]:
                    if xp != caseviste[i] or yp != caseviste[i + 1]:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                        xp = xMouse - (xMouse % GlobalVarG2.gpx)
                        yp = yMouse - (yMouse % GlobalVarG2.gpy)
                    casellaTrovata = True
                    break
                i += 3
            if not casellaTrovata:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i + 1] < xMouse < cofanetti[i + 1] + GlobalVarG2.gpx and cofanetti[i + 2] < yMouse < cofanetti[i + 2] + GlobalVarG2.gpy:
                        if xp != cofanetti[i + 1] or yp != cofanetti[i + 2]:
                            j = 0
                            while j < len(caseviste):
                                if ((cofanetti[i + 1] + GlobalVarG2.gpx == caseviste[j] and cofanetti[i + 2] == caseviste[j + 1]) or (cofanetti[i + 1] - GlobalVarG2.gpx == caseviste[j] and cofanetti[i + 2] == caseviste[j + 1]) or (cofanetti[i + 1] == caseviste[j] and cofanetti[i + 2] + GlobalVarG2.gpy == caseviste[j + 1]) or (cofanetti[i + 1] == caseviste[j] and cofanetti[i + 2] - GlobalVarG2.gpy == caseviste[j + 1])) and caseviste[j + 2]:
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                                    xp = xMouse - (xMouse % GlobalVarG2.gpx)
                                    yp = yMouse - (yMouse % GlobalVarG2.gpy)
                                    break
                                j += 3
                        casellaTrovata = True
                        break
                    i += 4
            if not casellaTrovata:
                i = 0
                while i < len(porte):
                    if porte[i + 1] < xMouse < porte[i + 1] + GlobalVarG2.gpx and porte[i + 2] < yMouse < porte[i + 2] + GlobalVarG2.gpy:
                        if xp != porte[i + 1] or yp != porte[i + 2]:
                            j = 0
                            while j < len(caseviste):
                                if ((porte[i + 1] + GlobalVarG2.gpx == caseviste[j] and porte[i + 2] == caseviste[j + 1]) or (porte[i + 1] - GlobalVarG2.gpx == caseviste[j] and porte[i + 2] == caseviste[j + 1]) or (porte[i + 1] == caseviste[j] and porte[i + 2] + GlobalVarG2.gpy == caseviste[j + 1]) or (porte[i + 1] == caseviste[j] and porte[i + 2] - GlobalVarG2.gpy == caseviste[j + 1])) and caseviste[j + 2]:
                                    puntaPorta = True
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                                    xp = xMouse - (xMouse % GlobalVarG2.gpx)
                                    yp = yMouse - (yMouse % GlobalVarG2.gpy)
                                    break
                                j += 3
                        casellaTrovata = True
                        break
                    i += 4
        if GlobalVarG2.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / Rallo / Colco / personaggio / porta / cofanetto / nemico / casella nel raggio (in caso di oggetto)
            if GlobalVarG2.gsy // 18 * 17 < yMouse < GlobalVarG2.gsy and GlobalVarG2.gsx // 32 * 0 < xMouse < GlobalVarG2.gsx // 32 * 6:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or not nemicoInquadrato) and 0 < yMouse < GlobalVarG2.gsy // 18 * 1 and GlobalVarG2.gsx // 32 * 0 < xMouse < GlobalVarG2.gsx // 32 * 4:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 < yMouse < GlobalVarG2.gsy // 18 * 1 and GlobalVarG2.gsx // 32 * 0 < xMouse < GlobalVarG2.gsx // 32 * 1:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 < yMouse < GlobalVarG2.gsy // 18 * 1 and GlobalVarG2.gsx // 32 * 0 < xMouse < GlobalVarG2.gsx // 32 * 3:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif GlobalVarG2.gsy // 18 * 0 < yMouse < GlobalVarG2.gsy // 18 * 1.5 and GlobalVarG2.gsx // 32 * 28 < xMouse < GlobalVarG2.gsx // 32 * 30:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            elif y < yMouse < y + GlobalVarG2.gpy and x < xMouse < x + GlobalVarG2.gpx:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "Rallo"
            elif ry < yMouse < ry + GlobalVarG2.gpy and rx < xMouse < rx + GlobalVarG2.gpx:
                if GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(False)
                inquadratoQualcosa = "Colco"
            else:
                if not inquadratoQualcosa:
                    for personaggio in listaPersonaggi:
                        if personaggio.x < xMouse < personaggio.x + GlobalVarG2.gpx and personaggio.y < yMouse < personaggio.y + GlobalVarG2.gpy:
                            if (personaggio.x == x + GlobalVarG2.gpx and personaggio.y == y) or (personaggio.x == x - GlobalVarG2.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalVarG2.gpy) or (personaggio.x == x and personaggio.y == y - GlobalVarG2.gpy):
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "personaggio"
                            break
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] < xMouse < porte[i + 1] + GlobalVarG2.gpx and porte[i + 2] < yMouse < porte[i + 2] + GlobalVarG2.gpy:
                            if (porte[i + 1] == x + GlobalVarG2.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalVarG2.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalVarG2.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalVarG2.gpy):
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "porta"
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] < xMouse < cofanetti[i + 1] + GlobalVarG2.gpx and cofanetti[i + 2] < yMouse < cofanetti[i + 2] + GlobalVarG2.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalVarG2.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalVarG2.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalVarG2.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalVarG2.gpy)) and not cofanetti[i + 3]:
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto"
                            break
                        i += 4
                if not inquadratoQualcosa:
                    for nemico in listaNemiciVisti:
                        if nemico.x < xMouse < nemico.x + GlobalVarG2.gpx and nemico.y < yMouse < nemico.y + GlobalVarG2.gpy:
                            if nemicoInquadrato and type(nemicoInquadrato) is not str and nemico.x == nemicoInquadrato.x and nemico.y == nemicoInquadrato.y:
                                j = 0
                                while j < len(caseattactot):
                                    if caseattactot[j] == nemico.x and caseattactot[j + 1] == nemico.y:
                                        if caseattactot[j + 2]:
                                            if GlobalVarG2.mouseBloccato:
                                                GlobalVarG2.configuraCursore(False)
                                            inquadratoQualcosa = "nemico"
                                        break
                                    j += 3
                            else:
                                j = 0
                                while j < len(caseviste):
                                    if caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y:
                                        if caseviste[j + 2]:
                                            if GlobalVarG2.mouseBloccato:
                                                GlobalVarG2.configuraCursore(False)
                                            inquadratoQualcosa = "nemico"
                                        break
                                    j += 3
                            break
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(vitaesca):
                        if vitaesca[i + 2] < xMouse < vitaesca[i + 2] + GlobalVarG2.gpx and vitaesca[i + 3] < yMouse < vitaesca[i + 3] + GlobalVarG2.gpy:
                            if nemicoInquadrato and type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                                idEscaInquadrata = int(nemicoInquadrato[4:])
                                j = 0
                                while j < len(vitaesca):
                                    if idEscaInquadrata == vitaesca[j]:
                                        if not (vitaesca[i + 2] == vitaesca[j + 2] and vitaesca[i + 3] == vitaesca[j + 3]):
                                            if GlobalVarG2.mouseBloccato:
                                                GlobalVarG2.configuraCursore(False)
                                            inquadratoQualcosa = "esca"
                                        break
                                    j += 4
                            else:
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "esca"
                            break
                        i += 4
                if not inquadratoQualcosa and attacco > 1:
                    if x - GlobalVarG2.gpx * raggioDiLancio <= xMouse <= x + GlobalVarG2.gpx + GlobalVarG2.gpx * raggioDiLancio and y - GlobalVarG2.gpy * raggioDiLancio <= yMouse <= y + GlobalVarG2.gpy + GlobalVarG2.gpy * raggioDiLancio:
                        i = 0
                        while i < len(caseattactot):
                            if caseattactot[i] <= xMouse <= caseattactot[i] + GlobalVarG2.gpx and caseattactot[i + 1] <= yMouse <= caseattactot[i + 1] + GlobalVarG2.gpy and caseattactot[i + 2]:
                                if GlobalVarG2.mouseBloccato:
                                    GlobalVarG2.configuraCursore(False)
                                inquadratoQualcosa = "casellaNelRaggio"
                                break
                            i += 3
        if not inquadratoQualcosa:
            if not GlobalVarG2.mouseBloccato:
                GlobalVarG2.configuraCursore(True)

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
            if event.type == pygame.KEYDOWN:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                # esci
                if event.key == pygame.K_q:
                    risposta = True
                    sposta = False
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                # esci e apri il menu
                if event.key == pygame.K_ESCAPE:
                    risposta = True
                    sposta = False
                    startf = True

                # attiva / disattiva il gambit
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoTeleColco)
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True

                # scorrere il puntatore sui nemici / GlobalVarG2.esche / Colco
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    nemicoInquadratoTemp = False
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                    # seleziono i nemici / GlobalVarG2.esche visti/e + controllo se il puntatore è su un nemico / esca / Colco
                    listaNemiciVisti = []
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            listaNemiciVisti.append(nemico)
                            if nemico.x == xp and nemico.y == yp:
                                nemicoInquadratoTemp = nemico
                    listaEscheViste = []
                    i = 0
                    while i < len(vitaesca):
                        j = 0
                        while j < len(caseviste):
                            if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and caseviste[j + 2]:
                                listaEscheViste.append(vitaesca[i])
                                listaEscheViste.append(vitaesca[i + 1])
                                listaEscheViste.append(vitaesca[i + 2])
                                listaEscheViste.append(vitaesca[i + 3])
                                if vitaesca[i + 2] == xp and vitaesca[i + 3] == yp:
                                    nemicoInquadratoTemp = "Esca" + str(vitaesca[i])
                            j += 3
                        i += 4
                    if rx == xp and ry == yp:
                        nemicoInquadratoTemp = "Colco"

                    if not nemicoInquadratoTemp:
                        if type(nemicoInquadrato) is str and nemicoInquadrato == "Colco":
                            xp = rx
                            yp = ry
                        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
                            xp = nemicoInquadrato.x
                            yp = nemicoInquadrato.y
                        elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                            i = 0
                            while i < len(vitaesca):
                                if nemicoInquadratoTemp[4:] == vitaesca[i]:
                                    xp = vitaesca[i + 2]
                                    yp = vitaesca[i + 3]
                                    break
                                i += 4
                        else:
                            xp = rx
                            yp = ry
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp == "Colco":
                        if len(listaNemiciVisti) > 0:
                            xp = listaNemiciVisti[0].x
                            yp = listaNemiciVisti[0].y
                        elif len(listaEscheViste) > 0:
                            xp = listaEscheViste[2]
                            yp = listaEscheViste[3]
                        else:
                            xp = rx
                            yp = ry
                    elif not type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp:
                        if len(listaNemiciVisti) > 0 and listaNemiciVisti.index(nemicoInquadratoTemp) < len(listaNemiciVisti) - 1:
                            xp = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadratoTemp) + 1].x
                            yp = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadratoTemp) + 1].y
                        elif len(listaEscheViste) > 0:
                            xp = listaEscheViste[2]
                            yp = listaEscheViste[3]
                        else:
                            xp = rx
                            yp = ry
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                        if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 3 < len(listaEscheViste) - 1:
                            xp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 4 + 2]
                            yp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 4 + 3]
                        else:
                            xp = rx
                            yp = ry
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    nemicoInquadratoTemp = False
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                    # seleziono i nemici / GlobalVarG2.esche visti/e + controllo se il puntatore è su un nemico / esca / Colco
                    listaNemiciVisti = []
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            listaNemiciVisti.append(nemico)
                            if nemico.x == xp and nemico.y == yp:
                                nemicoInquadratoTemp = nemico
                    listaEscheViste = []
                    i = 0
                    while i < len(vitaesca):
                        j = 0
                        while j < len(caseviste):
                            if caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] and caseviste[j + 2]:
                                listaEscheViste.append(vitaesca[i])
                                listaEscheViste.append(vitaesca[i + 1])
                                listaEscheViste.append(vitaesca[i + 2])
                                listaEscheViste.append(vitaesca[i + 3])
                                if vitaesca[i + 2] == xp and vitaesca[i + 3] == yp:
                                    nemicoInquadratoTemp = "Esca" + str(vitaesca[i])
                            j += 3
                        i += 4
                    if rx == xp and ry == yp:
                        nemicoInquadratoTemp = "Colco"

                    if not nemicoInquadratoTemp:
                        if type(nemicoInquadrato) is str and nemicoInquadrato == "Colco":
                            xp = rx
                            yp = ry
                        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
                            xp = nemicoInquadrato.x
                            yp = nemicoInquadrato.y
                        elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                            i = 0
                            while i < len(vitaesca):
                                if nemicoInquadratoTemp[4:] == vitaesca[i]:
                                    xp = vitaesca[i + 2]
                                    yp = vitaesca[i + 3]
                                    break
                                i += 4
                        else:
                            xp = rx
                            yp = ry
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp == "Colco":
                        if len(listaEscheViste) > 0:
                            xp = listaEscheViste[len(listaEscheViste) - 4 + 2]
                            yp = listaEscheViste[len(listaEscheViste) - 4 + 3]
                        elif len(listaNemiciVisti) > 0:
                            xp = listaNemiciVisti[len(listaNemiciVisti) - 1].x
                            yp = listaNemiciVisti[len(listaNemiciVisti) - 1].y
                        else:
                            xp = rx
                            yp = ry
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                        if len(listaEscheViste) > 0 and listaEscheViste.index(int(nemicoInquadratoTemp[4:])) != 0:
                            xp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) - 4 + 2]
                            yp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) - 4 + 3]
                        elif len(listaNemiciVisti) > 0:
                            xp = listaNemiciVisti[len(listaNemiciVisti) - 1].x
                            yp = listaNemiciVisti[len(listaNemiciVisti) - 1].y
                        else:
                            xp = rx
                            yp = ry
                    elif not type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp:
                        if len(listaNemiciVisti) > 0 and listaNemiciVisti.index(nemicoInquadratoTemp) != 0:
                            xp = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadratoTemp) - 1].x
                            yp = listaNemiciVisti[listaNemiciVisti.index(nemicoInquadratoTemp) - 1].y
                        else:
                            xp = rx
                            yp = ry

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
                    if selezioneAvvenuta:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selObbiettivo)
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if event.key == pygame.K_w:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nyp = -GlobalVarG2.gpy
                    nxp = 0
                if event.key == pygame.K_a:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nxp = -GlobalVarG2.gpx
                    nyp = 0
                if event.key == pygame.K_s:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nyp = GlobalVarG2.gpy
                    nxp = 0
                if event.key == pygame.K_d:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nxp = GlobalVarG2.gpx
                    nyp = 0
                # attacco
                if event.key == pygame.K_SPACE:
                    sposta = False
                    if attacco != 0:
                        attaccoConfermato = True

            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not startf:
                tastop = "mouseDestro"
                risposta = True
                sposta = False
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and centraleMouse and not startf:
                tastop = "mouseCentrale"
                risposta = True
                sposta = False
                startf = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and not startf:
                tastop = "mouseSinistro"
                if inquadratoQualcosa == "start":
                    startf = True
                elif inquadratoQualcosa == "battaglia":
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
                    sposta = False
                elif inquadratoQualcosa == "telecolco":
                    GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.suonoTeleColco)
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                elif inquadratoQualcosa == "Rallo":
                    difesa = 2
                    risposta = True
                elif inquadratoQualcosa == "Colco":
                    spingiColco = True
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                elif inquadratoQualcosa == "porta":
                    apriChiudiPorta = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                elif inquadratoQualcosa == "cofanetto":
                    apriCofanetto = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                elif inquadratoQualcosa == "personaggio":
                    interagisciConPersonaggio = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                elif inquadratoQualcosa == "nemico":
                    sposta = False
                    if attacco != 0:
                        attaccoConfermato = True
                elif inquadratoQualcosa == "esca":
                    sposta = False
                    if attacco != 0:
                        attaccoConfermato = True
                elif inquadratoQualcosa == "casellaNelRaggio":
                    sposta = False
                    if attacco != 0:
                        attaccoConfermato = True
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
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
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if attaccoConfermato:
            attaccoConfermato = False
            daInquadrare = False
            if tastop == "mouseSinistro" and attacco == 1 and (inquadratoQualcosa == "nemico" or inquadratoQualcosa == "esca"):
                if inquadratoQualcosa == "nemico" and not (nemicoInquadrato and type(nemicoInquadrato) is not str and xp == nemicoInquadrato.x and yp == nemicoInquadrato.y):
                    for nemico in listaNemici:
                        if xp == nemico.x and yp == nemico.y:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selObbiettivo)
                            nemicoInquadrato = nemico
                            daInquadrare = True
                            break
                if inquadratoQualcosa == "esca":
                    if not (nemicoInquadrato and type(nemicoInquadrato) is str and nemicoInquadrato.startswith("esca")):
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selObbiettivo)
                        nemicoInquadrato = "Esca" + str(vitaesca[i])
                        daInquadrare = True
                    else:
                        idEscaInquadrata = int(nemicoInquadrato[4:])
                        i = 0
                        while i < len(vitaesca):
                            if idEscaInquadrata == vitaesca[i]:
                                if not (xp == vitaesca[i + 2] and yp == vitaesca[i + 3]):
                                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selObbiettivo)
                                    nemicoInquadrato = "Esca" + str(vitaesca[i])
                                    daInquadrare = True
                                break
                            i += 4
            if not daInquadrare:
                infliggidanno = False
                statom = 0
                raggio = 0
                suPersonaggio = False
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        suPersonaggio = True
                        break
                # interagisci con personaggi attacco = 1
                if attacco == 1 and ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and suPersonaggio:
                    interagisciConPersonaggio = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                # spingi Colco attacco = 1
                if attacco == 1 and ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and (xp == rx and yp == ry):
                    spingiColco = True
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                # apri/chiudi porta attacco = 1
                elif attacco == 1 and ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and suPorta:
                    apriChiudiPorta = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                # apri cofanetto attacco = 1
                elif attacco == 1 and ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and suCofanetto:
                    apriCofanetto = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                # attacco ravvicinato attacco = 1
                elif attacco == 1 and ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)):
                    infliggidanno = True
                    danno = attVicino
                    raggio = GlobalVarG2.gpx * 0
                # attacco lontano attacco = 1
                elif attacco == 1 and not ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy) or (xp == x and yp == y) or (xp == rx and yp == ry)) and numFrecce > 0:
                    j = 0
                    while j < len(caseattactot):
                        if caseattactot[j] == xp and caseattactot[j + 1] == yp:
                            if caseattactot[j + 2]:
                                infliggidanno = True
                                danno = attLontano
                                raggio = GlobalVarG2.gpx * 0
                            break
                        j += 3
                # difesa attacco = 1
                elif attacco == 1 and (xp == x and yp == y):
                    difesa = 2
                    risposta = True
                # bomba attacco = 2
                if attacco == 2 and (abs(x - xp) <= GlobalVarG2.gpx * 6 and abs(y - yp) <= GlobalVarG2.gpy * 6):
                    # controllo caselle attaccabili
                    continua = True
                    # disegno le caselle attaccabili
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                            continua = False
                            break
                        i = i + 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
                            if xp > x:
                                npers = 1
                            else:
                                npers = 2
                        elif abs(yp - y) > abs(xp - x) or (abs(xp - x) == abs(yp - y) and n == 2):
                            if yp > y:
                                npers = 4
                            else:
                                npers = 3
                        animaOggetto[0] = "bomba"
                        animaOggetto[1] = xp
                        animaOggetto[2] = yp
                        attaccato = True
                        infliggidanno = True
                        danno = 10
                        raggio = GlobalVarG2.gpx * 1
                        sposta = True
                        risposta = True
                # bomba veleno attacco = 3
                if attacco == 3 and (abs(x - xp) <= GlobalVarG2.gpx * 5 and abs(y - yp) <= GlobalVarG2.gpy * 5):
                    # controllo caselle attaccabili
                    continua = True
                    # disegno le caselle attaccabili
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                            continua = False
                            break
                        i = i + 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
                            if xp > x:
                                npers = 1
                            else:
                                npers = 2
                        elif abs(yp - y) > abs(xp - x) or (abs(xp - x) == abs(yp - y) and n == 2):
                            if yp > y:
                                npers = 4
                            else:
                                npers = 3
                        animaOggetto[0] = "bombaVeleno"
                        animaOggetto[1] = xp
                        animaOggetto[2] = yp
                        attaccato = True
                        infliggidanno = True
                        danno = 20
                        statom = 1
                        raggio = GlobalVarG2.gpx * 0
                        sposta = True
                        risposta = True
                # esca attacco = 4
                if attacco == 4 and (abs(x - xp) <= GlobalVarG2.gpx * 6 and abs(y - yp) <= GlobalVarG2.gpy * 6):
                    # controllo caselle attaccabili
                    continua = True
                    # disegno le caselle attaccabili
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                            continua = False
                            break
                        i = i + 3
                    if continua:
                        # conferma lancio GlobalVarG2.esche
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
                            n = random.randint(1, 2)
                            if abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
                                if xp > x:
                                    npers = 1
                                else:
                                    npers = 2
                            elif abs(yp - y) > abs(xp - x) or (abs(xp - x) == abs(yp - y) and n == 2):
                                if yp > y:
                                    npers = 4
                                else:
                                    npers = 3
                            animaOggetto[0] = "esca"
                            animaOggetto[1] = xp
                            animaOggetto[2] = yp
                            attaccato = True
                            infliggidanno = True
                            danno = 0
                            raggio = 0
                            creaesca = True
                            sposta = True
                            risposta = True
                # bomba appiccicosa attacco = 5
                if attacco == 5 and (abs(x - xp) <= GlobalVarG2.gpx * 5 and abs(y - yp) <= GlobalVarG2.gpy * 5):
                    # controllo caselle attaccabili
                    continua = True
                    # disegno le caselle attaccabili
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                            continua = False
                            break
                        i = i + 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
                            if xp > x:
                                npers = 1
                            else:
                                npers = 2
                        elif abs(yp - y) > abs(xp - x) or (abs(xp - x) == abs(yp - y) and n == 2):
                            if yp > y:
                                npers = 4
                            else:
                                npers = 3
                        animaOggetto[0] = "bombaAppiccicosa"
                        animaOggetto[1] = xp
                        animaOggetto[2] = yp
                        attaccato = True
                        infliggidanno = True
                        danno = 20
                        statom = 2
                        raggio = GlobalVarG2.gpx * 0
                        sposta = True
                        risposta = True
                # bomba potenziata attacco = 6
                if attacco == 6 and (abs(x - xp) <= GlobalVarG2.gpx * 4 and abs(y - yp) <= GlobalVarG2.gpy * 4):
                    # controllo caselle attaccabili
                    continua = True
                    # disegno le caselle attaccabili
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                            continua = False
                            break
                        i = i + 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
                            if xp > x:
                                npers = 1
                            else:
                                npers = 2
                        elif abs(yp - y) > abs(xp - x) or (abs(xp - x) == abs(yp - y) and n == 2):
                            if yp > y:
                                npers = 4
                            else:
                                npers = 3
                        animaOggetto[0] = "bombaPotenziata"
                        animaOggetto[1] = xp
                        animaOggetto[2] = yp
                        attaccato = True
                        infliggidanno = True
                        danno = 200
                        raggio = GlobalVarG2.gpx * 2
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

                        attaccoDiRallo.append(nemico)
                        dannoApprossimato = danno - nemico.difesa
                        if dannoApprossimato < 0:
                            dannoApprossimato = 0
                        attaccoDiRallo.append(-dannoApprossimato)
                        if attacco == 3:
                            attaccoDiRallo.append("avvelena")
                        elif attacco == 5:
                            attaccoDiRallo.append("appiccica")
                        else:
                            attaccoDiRallo.append("")

                        sposta = True
                        risposta = True

                # attacco da vicino
                if attacco == 1 and ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and sposta and risposta and infliggidanno:
                    attaccato = True
                    if xp == x + GlobalVarG2.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVarG2.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVarG2.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVarG2.gpy:
                        npers = 3
                # attacco con arco
                elif attacco == 1 and not ((xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and sposta and risposta and infliggidanno:
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
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)

        if ricaricaschermo and not appenaCaricato:
            GlobalVarG2.schermo.blit(stanzaa, (0, 0))
            # porte
            i = 0
            while i < len(porte):
                if not porte[i + 3]:
                    vmurx = porte[i + 1]
                    vmury = porte[i + 2]
                    murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, GlobalVarG2.gpx, 0, stanza, False, False, False, porte, cofanetti)
                    GlobalVarG2.schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
                    if vmurx == murx and vmury == mury:
                        GlobalVarG2.schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
                    else:
                        GlobalVarG2.schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
                i = i + 4
            # cofanetti
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
                    j = j + 3
                i = i + 4
            # background occhio/chiave
            GlobalVarG2.schermo.blit(GlobalVarG2.sfochiaveocchio, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 5), 0))
            # vista nemici
            if apriocchio:
                GlobalVarG2.schermo.blit(GlobalVarG2.occhioape, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.occhiochiu, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))
            # chiave robo
            if chiamarob:
                GlobalVarG2.schermo.blit(GlobalVarG2.chiaveroboacc, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.chiaverobospe, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))
            # disegno le caselle viste
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2]:
                    if ((caseviste[i] / GlobalVarG2.gpx) + (caseviste[i + 1] / GlobalVarG2.gpy)) % 2 == 0:
                        GlobalVarG2.schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                    if ((caseviste[i] / GlobalVarG2.gpx) + (caseviste[i + 1] / GlobalVarG2.gpy)) % 2 == 1:
                        GlobalVarG2.schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                i += 3
            ricaricaschermo = False
            appenaCaricato = True

        # disegno la casella sotto i nemici e Colco
        for nemico in listaNemici:
            if nemico.inCasellaVista:
                if ((nemico.x / GlobalVarG2.gpx) + (nemico.y / GlobalVarG2.gpy)) % 2 == 0:
                    GlobalVarG2.schermo.blit(sfondinoa, (nemico.x, nemico.y))
                if ((nemico.x / GlobalVarG2.gpx) + (nemico.y / GlobalVarG2.gpy)) % 2 == 1:
                    GlobalVarG2.schermo.blit(sfondinob, (nemico.x, nemico.y))
        if ((rx / GlobalVarG2.gpx) + (ry / GlobalVarG2.gpy)) % 2 == 0:
            GlobalVarG2.schermo.blit(sfondinoa, (rx, ry))
        if ((rx / GlobalVarG2.gpx) + (ry / GlobalVarG2.gpy)) % 2 == 1:
            GlobalVarG2.schermo.blit(sfondinob, (rx, ry))

        # disegno le caselle attaccabili
        i = 0
        while i < len(caseattactot):
            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                GlobalVarG2.schermo.blit(GlobalVarG2.caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
            i = i + 3
        # visualizza campo attaccabile se sto usando un oggetto
        if attacco == 2:
            campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabile2, (GlobalVarG2.gpx * 13, GlobalVarG2.gpy * 13))
            GlobalVarG2.schermo.blit(campoattaccabile3, (x - (GlobalVarG2.gpx * 6), y - (GlobalVarG2.gpy * 6)))
        if attacco == 3:
            campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabile2, (GlobalVarG2.gpx * 11, GlobalVarG2.gpy * 11))
            GlobalVarG2.schermo.blit(campoattaccabile3, (x - (GlobalVarG2.gpx * 5), y - (GlobalVarG2.gpy * 5)))
        if attacco == 4:
            campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabile2, (GlobalVarG2.gpx * 13, GlobalVarG2.gpy * 13))
            GlobalVarG2.schermo.blit(campoattaccabile3, (x - (GlobalVarG2.gpx * 6), y - (GlobalVarG2.gpy * 6)))
        if attacco == 5:
            campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabile2, (GlobalVarG2.gpx * 11, GlobalVarG2.gpy * 11))
            GlobalVarG2.schermo.blit(campoattaccabile3, (x - (GlobalVarG2.gpx * 5), y - (GlobalVarG2.gpy * 5)))
        if attacco == 6:
            campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabile2, (GlobalVarG2.gpx * 9, GlobalVarG2.gpy * 9))
            GlobalVarG2.schermo.blit(campoattaccabile3, (x - (GlobalVarG2.gpx * 4), y - (GlobalVarG2.gpy * 4)))

        # disegna porte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                vmurx = porte[i + 1]
                vmury = porte[i + 2]
                murx, mury, inutile, inutile, inutile = muri_porte(vmurx, vmury, GlobalVarG2.gpx, 0, stanza, False, False, False, porte, cofanetti)
                GlobalVarG2.schermo.blit(sfondinoc, (porte[i + 1], porte[i + 2]))
                if vmurx == murx and vmury == mury:
                    GlobalVarG2.schermo.blit(portaOriz, (porte[i + 1], porte[i + 2]))
                else:
                    GlobalVarG2.schermo.blit(portaVert, (porte[i + 1], porte[i + 2]))
            i = i + 4
        # disegna cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - GlobalVarG2.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                        caseviste[j] == cofanetti[i + 1] + GlobalVarG2.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVarG2.gpy) or (
                            caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVarG2.gpy)) and \
                        caseviste[j + 2]:
                    GlobalVarG2.schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                    if cofanetti[i + 3]:
                        GlobalVarG2.schermo.blit(GlobalVarG2.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        GlobalVarG2.schermo.blit(GlobalVarG2.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j = j + 3
            i = i + 4

        # movimenti del puntatore su porte e cofanetti quando si usa la tastiera
        if not GlobalVarG2.mouseVisibile:
            # mettere il puntatore su porte
            i = 0
            while i < len(porte):
                if porte[i + 1] == xp + nxp and porte[i + 2] == yp + nyp and not porte[i + 3]:
                    if nxp != 0 or nyp != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
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
                    if nxp != 0 or nyp != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                    puntaCofanetto = True
                    xp = xp + nxp
                    yp = yp + nyp
                    break
                i = i + 4
            # movimento inquadra (ultimi 4 inutili)
            if not puntaPorta and not puntaCofanetto:
                xp, yp, stanza, inutile, cambiosta = muri_porte(xp, yp, nxp, nyp, stanza, False, True, False, porte, cofanetti)
                if xp != xvp or yp != yvp:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
            # movimento inquadra quando si è sulle porte
            if puntaPorta:
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == xp + nxp and caseviste[i + 1] == yp + nyp:
                        if caseviste[i + 2]:
                            if nxp != 0 or nyp != 0:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostaPunBattaglia)
                            xp = xp + nxp
                            yp = yp + nyp
                            puntaPorta = False
                            break
                    i = i + 3

        # GlobalVarG2.esche: id, vita, xesca, yesca
        i = 0
        while i < len(vitaesca):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == vitaesca[i + 2] - GlobalVarG2.gpx and caseviste[j + 1] == vitaesca[i + 3]) or (caseviste[j] == vitaesca[i + 2] + GlobalVarG2.gpx and caseviste[j + 1] == vitaesca[i + 3]) or (caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] - GlobalVarG2.gpy) or (caseviste[j] == vitaesca[i + 2] and caseviste[j + 1] == vitaesca[i + 3] + GlobalVarG2.gpy)) and caseviste[j + 2]:
                    if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 0:
                        GlobalVarG2.schermo.blit(sfondinoa, (vitaesca[i + 2], vitaesca[i + 3]))
                    if ((vitaesca[i + 2] / GlobalVarG2.gpx) + (vitaesca[i + 3] / GlobalVarG2.gpy)) % 2 == 1:
                        GlobalVarG2.schermo.blit(sfondinob, (vitaesca[i + 2], vitaesca[i + 3]))
                    GlobalVarG2.schermo.blit(GlobalVarG2.esche, (vitaesca[i + 2], vitaesca[i + 3]))
                    break
                j += 3
            i += 4

        # denaro: qta, x, y
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

        # robo (anche in caso di raffreddamento e autoricarica)
        if raffredda > 0:
            GlobalVarG2.schermo.blit(armrobS, (rx, ry))
            GlobalVarG2.schermo.blit(GlobalVarG2.robos, (rx, ry))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVarG2.vetAnimazioniTecniche):
                if GlobalVarG2.vetAnimazioniTecniche[i] == "raffred":
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
        elif autoRic1 > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (rx, ry))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVarG2.vetAnimazioniTecniche):
                if GlobalVarG2.vetAnimazioniTecniche[i] == "ricarica":
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
        elif autoRic2 > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.robomo, (rx, ry))
            imgAnimazione = 0
            i = 0
            while i < len(GlobalVarG2.vetAnimazioniTecniche):
                if GlobalVarG2.vetAnimazioniTecniche[i] == "ricarica+":
                    imgAnimazione = GlobalVarG2.vetAnimazioniTecniche[i + 1][0]
                    break
                i += 2
            GlobalVarG2.schermo.blit(imgAnimazione, (rx, ry))
        else:
            GlobalVarG2.schermo.blit(robot, (rx, ry))
            if surrisc > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.roboSurrisc, (rx, ry))
            GlobalVarG2.schermo.blit(armrob, (rx, ry))

        # personaggio
        if not risposta:
            disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

        # disegno tutti i personaggi
        for personaggio in listaPersonaggi:
            j = 0
            while j < len(caseviste):
                if caseviste[j] == personaggio.x and caseviste[j + 1] == personaggio.y and caseviste[j + 2]:
                    GlobalVarG2.schermo.blit(personaggio.imgAttuale, (personaggio.x, personaggio.y))
                    break
                j += 3

        # disegnare i mostri
        j = 0
        while j < len(caseviste):
            for nemico in listaNemici:
                if caseviste[j] == nemico.x and caseviste[j + 1] == nemico.y and caseviste[j + 2]:
                    GlobalVarG2.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
                    if nemico.appiccicato:
                        GlobalVarG2.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))
                    if nemico.avvelenato:
                        GlobalVarG2.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
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
                        if (xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy):
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
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        suPorta = False
                        suCofanetto = False
                        puntatogg = puntatogg7
                        break
            if (((xp == x and yp == y) or (xp == x + GlobalVarG2.gpx and yp == y) or (xp == x - GlobalVarG2.gpx and yp == y) or (xp == x and yp == y + GlobalVarG2.gpy) or (xp == x and yp == y - GlobalVarG2.gpy)) and puntatogg != 0) or (puntatogg == puntatogg6 and nemicoInCampoVisivoArco and numFrecce > 0):
                puntat = GlobalVarG2.puntatIn
            else:
                puntat = GlobalVarG2.puntatOut
        if attacco == 2:
            if abs(x - xp) <= GlobalVarG2.gpx * 6 and abs(y - yp) <= GlobalVarG2.gpy * 6:
                puntat = GlobalVarG2.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = GlobalVarG2.puntatOut
                    i = i + 3
            else:
                puntat = GlobalVarG2.puntatOut
        if attacco == 3:
            if abs(x - xp) <= GlobalVarG2.gpx * 5 and abs(y - yp) <= GlobalVarG2.gpy * 5:
                puntat = GlobalVarG2.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = GlobalVarG2.puntatOut
                    i = i + 3
            else:
                puntat = GlobalVarG2.puntatOut
        if attacco == 4:
            if abs(x - xp) <= GlobalVarG2.gpx * 6 and abs(y - yp) <= GlobalVarG2.gpy * 6:
                puntat = GlobalVarG2.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = GlobalVarG2.puntatOut
                        break
                    i = i + 3
                i = 0
                while i < len(vettoreDenaro):
                    if vettoreDenaro[i + 1] == xp and vettoreDenaro[i + 2] == yp:
                        puntat = GlobalVarG2.puntatOut
                        break
                    i += 3
            else:
                puntat = GlobalVarG2.puntatOut
        if attacco == 5:
            if abs(x - xp) <= GlobalVarG2.gpx * 5 and abs(y - yp) <= GlobalVarG2.gpy * 5:
                puntat = GlobalVarG2.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = GlobalVarG2.puntatOut
                    i = i + 3
            else:
                puntat = GlobalVarG2.puntatOut
        if attacco == 6:
            if abs(x - xp) <= GlobalVarG2.gpx * 4 and abs(y - yp) <= GlobalVarG2.gpy * 4:
                puntat = GlobalVarG2.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                        puntat = GlobalVarG2.puntatOut
                    i = i + 3
            else:
                puntat = GlobalVarG2.puntatOut
        GlobalVarG2.schermo.blit(puntat, (xp, yp))
        if puntatogg != 0:
            GlobalVarG2.schermo.blit(puntatogg, (xp, yp))
        if risposta:
            if ((xp / GlobalVarG2.gpx) + (yp / GlobalVarG2.gpy)) % 2 == 0:
                GlobalVarG2.schermo.blit(sfondinoa, (xp, yp))
            if ((xp / GlobalVarG2.gpx) + (yp / GlobalVarG2.gpy)) % 2 == 1:
                GlobalVarG2.schermo.blit(sfondinob, (xp, yp))

        # backbround occhio/chiave
        GlobalVarG2.schermo.blit(GlobalVarG2.sfochiaveocchio, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 5), 0))
        # vista nemici
        if apriocchio:
            GlobalVarG2.schermo.blit(GlobalVarG2.occhioape, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))
        else:
            GlobalVarG2.schermo.blit(GlobalVarG2.occhiochiu, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4 // 3), GlobalVarG2.gpy // 3))
        # chiave robo
        if chiamarob:
            GlobalVarG2.schermo.blit(GlobalVarG2.chiaveroboacc, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))
        else:
            GlobalVarG2.schermo.blit(GlobalVarG2.chiaverobospe, (GlobalVarG2.gsx - (GlobalVarG2.gpx * 4), 0))

        # vita-status rallo
        lungvitatot = int(((GlobalVarG2.gpx * pvtot) / float(4)) // 5)
        lungvita = (lungvitatot * pv) // pvtot
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
        messaggio("x " + str(numFrecce), GlobalVarG2.grigiochi, int(GlobalVarG2.gsx // 32 * 1.8), int(GlobalVarG2.gsy // 18 * 17.2), 40)
        if avvele:
            GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gsx // 32 * 3, GlobalVarG2.gsy // 18 * 17))
        if attp > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.attaccopiu, (GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 17))
        if difp > 0:
            GlobalVarG2.schermo.blit(GlobalVarG2.difesapiu, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 17))

        puntandoSuUnNemicoOColcoOEsca = False
        # disegna vita GlobalVarG2.esche
        i = 0
        while i < len(vitaesca):
            if xp == vitaesca[i + 2] and yp == vitaesca[i + 3]:
                puntandoSuUnNemicoOColcoOEsca = True
                lungvita = int(((GlobalVarG2.gpx * vitaesca[i + 1]) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoEsche, (0, 0))
                GlobalVarG2.schermo.blit(GlobalVarG2.esche, (0, 0))
                indvitamost = pygame.transform.scale(GlobalVarG2.indvita, (int(((GlobalVarG2.gpx * 1000) / float(4)) // 15), GlobalVarG2.gpy // 4))
                fineindvitamost = pygame.transform.scale(GlobalVarG2.fineindvita, (GlobalVarG2.gpx // 12, GlobalVarG2.gpy // 4))
                vitaesche = pygame.transform.scale(GlobalVarG2.vitanemico0, (lungvita, GlobalVarG2.gpy // 4))
                GlobalVarG2.schermo.blit(indvitamost, (GlobalVarG2.gpx, 0))
                GlobalVarG2.schermo.blit(fineindvitamost, (GlobalVarG2.gpx + int(((GlobalVarG2.gpx * 1000) / float(4)) // 15), 0))
                GlobalVarG2.schermo.blit(vitaesche, (GlobalVarG2.gpx, 0))
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
                        GlobalVarG2.schermo.blit(GlobalVarG2.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabilemostro, ((raggiovista * 2) + GlobalVarG2.gpx, (raggiovista * 2) + GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoMostro, (0, 0))
                if nemico.avvelenato:
                    GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
                if nemico.appiccicato:
                    GlobalVarG2.schermo.blit(GlobalVarG2.appiccicoso, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
                GlobalVarG2.schermo.blit(nemico.imgS, (0, 0))
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
                ricaricaschermo = True
                break
        # vita-status-campo visivo robo
        if xp == rx and yp == ry:
            puntandoSuUnNemicoOColcoOEsca = True
            if enrob > 0:
                # controllo caselle attaccabili
                vistaRobo = GlobalVarG2.gpx * 8
                caseattactotRobo = trovacasattaccabili(rx, ry, stanza, porte, cofanetti, vistaRobo)
                # disegno le caselle attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        GlobalVarG2.schermo.blit(GlobalVarG2.caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabileRobo, ((vistaRobo * 2) + GlobalVarG2.gpx, (vistaRobo * 2) + GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(campoattaccabile3, (rx - vistaRobo, ry - vistaRobo))
                ricaricaschermo = True
            lungentot = int(((GlobalVarG2.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVarG2.gpx * enrob) / float(4)) // 15)
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
            if surrisc > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.surriscaldato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if velp > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.velocitapiu, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if effp > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.efficienzapiu, ((GlobalVarG2.gpx * 3) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
        # vita colco selezionato
        if nemicoInquadrato == "Colco" and not puntandoSuUnNemicoOColcoOEsca:
            if enrob > 0:
                # controllo caselle attaccabili
                vistaRobo = GlobalVarG2.gpx * 8
                caseattactotRobo = trovacasattaccabili(rx, ry, stanza, porte, cofanetti, vistaRobo)
                # disegno le caselle attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        GlobalVarG2.schermo.blit(GlobalVarG2.caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabileRobo, ((vistaRobo * 2) + GlobalVarG2.gpx, (vistaRobo * 2) + GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(campoattaccabile3, (rx - vistaRobo, ry - vistaRobo))
            lungentot = int(((GlobalVarG2.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVarG2.gpx * enrob) / float(4)) // 15)
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
            if surrisc > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.surriscaldato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if velp > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.velocitapiu, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if effp > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.efficienzapiu, ((GlobalVarG2.gpx * 3) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
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
                    GlobalVarG2.schermo.blit(GlobalVarG2.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(GlobalVarG2.campoattaccabilemostro,
                                                       ((raggiovista * 2) + GlobalVarG2.gpx, (raggiovista * 2) + GlobalVarG2.gpy))
            GlobalVarG2.schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoMostro, (0, 0))
            if nemicoInquadrato.avvelenato:
                GlobalVarG2.schermo.blit(GlobalVarG2.avvelenato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if nemicoInquadrato.appiccicato:
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
        # vita esca selezionata
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and not puntandoSuUnNemicoOColcoOEsca:
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vitaesca):
                if idEscaInquadrata == vitaesca[i]:
                    lungvita = int(((GlobalVarG2.gpx * vitaesca[i + 1]) / float(4)) // 15)
                    if lungvita < 0:
                        lungvita = 0
                    GlobalVarG2.schermo.blit(GlobalVarG2.sfondoEsche, (0, 0))
                    GlobalVarG2.schermo.blit(GlobalVarG2.esche, (0, 0))
                    indvitamost = pygame.transform.scale(GlobalVarG2.indvita, (int(((GlobalVarG2.gpx * 1000) / float(4)) // 15), GlobalVarG2.gpy // 4))
                    fineindvitamost = pygame.transform.scale(GlobalVarG2.fineindvita, (GlobalVarG2.gpx // 12, GlobalVarG2.gpy // 4))
                    vitaesche = pygame.transform.scale(GlobalVarG2.vitanemico0, (lungvita, GlobalVarG2.gpy // 4))
                    GlobalVarG2.schermo.blit(indvitamost, (GlobalVarG2.gpx, 0))
                    GlobalVarG2.schermo.blit(fineindvitamost, (GlobalVarG2.gpx + int(((GlobalVarG2.gpx * 1000) / float(4)) // 15), 0))
                    GlobalVarG2.schermo.blit(vitaesche, (GlobalVarG2.gpx, 0))
                    break
                i += 4
        # altrimenti mostro solo la vita di colco
        elif not puntandoSuUnNemicoOColcoOEsca:
            lungentot = int(((GlobalVarG2.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVarG2.gpx * enrob) / float(4)) // 15)
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
            if surrisc > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.surriscaldato, (GlobalVarG2.gpx + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if velp > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.velocitapiu, ((GlobalVarG2.gpx * 2) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))
            if effp > 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.efficienzapiu, ((GlobalVarG2.gpx * 3) + (GlobalVarG2.gpx // 8), GlobalVarG2.gpy // 4))

        # disegno img GlobalVarG2.puntatoreInquadraNemici
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

        if not risposta:
            pygame.display.update()
        elif not sposta or not attaccato:
            attacco = 0
        pygame.event.pump()
        GlobalVarG2.clockAttacco.tick(GlobalVarG2.fpsInquadra)

    return sposta, creaesca, xp, yp, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf
