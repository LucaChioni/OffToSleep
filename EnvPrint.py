# -*- coding: utf-8 -*-

from MovNemiciRob import *


def disegnaAmbiente(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, numFrecce, nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, primaDiAnima, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, avanzamentoStoria):
    if caricaTutto:
        GlobalVar.schermo.blit(imgSfondoStanza, (0, 0))
        # salvo la lista di cofanetti vicini a ceselle viste per non mettergli la casella oscurata
        vetCofanettiVisti = []
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                    vetCofanettiVisti.append(cofanetti[i + 1])
                    vetCofanettiVisti.append(cofanetti[i + 2])
                j += 3
            i += 4
        # disegno l'ombreggiatura delle caselle
        i = 0
        while i < len(casellePercorribili):
            if casellePercorribili[i + 2]:
                if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 0:
                    GlobalVar.schermo.blit(casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
                if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 1:
                    GlobalVar.schermo.blit(casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
            else:
                casellaNonOscurata = False
                j = 0
                while j < len(vetCofanettiVisti):
                    if casellePercorribili[i] == vetCofanettiVisti[j] and casellePercorribili[i + 1] == vetCofanettiVisti[j + 1]:
                        casellaNonOscurata = True
                    j += 2
                if casellaNonOscurata:
                    if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 0:
                        GlobalVar.schermo.blit(casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
                    if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 1:
                        GlobalVar.schermo.blit(casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
                else:
                    GlobalVar.schermo.blit(casellaOscurata, (casellePercorribili[i], casellePercorribili[i + 1]))
            i += 3

        # disegna porte
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
            i += 4
        # disegna cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                    if cofanetti[i + 3]:
                        GlobalVar.schermo.blit(GlobalVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        GlobalVar.schermo.blit(GlobalVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j += 3
            i += 4
    else:
        # disegnare casella sopra la vecchia posizione di rallo, colco, nemici e personaggi
        i = 0
        while i < len(vettoreImgCaselle):
            if vx == vettoreImgCaselle[i] and vy == vettoreImgCaselle[i + 1]:
                GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
            if vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
            for nemico in listaNemici:
                if nemico.inCasellaVista and nemico.vx == vettoreImgCaselle[i] and nemico.vy == vettoreImgCaselle[i + 1]:
                    GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                    disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
            for personaggio in listaPersonaggi:
                if (personaggio.inCasellaVista or personaggio.mantieniSempreASchermo) and personaggio.vx == vettoreImgCaselle[i] and personaggio.vy == vettoreImgCaselle[i + 1]:
                    GlobalVar.schermo.blit(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                    disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1], casellaChiara, casellaScura)
            i += 3

    # disegno la casella sopra la posizione di rallo, colco, personaggi e nemici
    c = 0
    while c < len(vettoreImgCaselle):
        if x == vettoreImgCaselle[c] and y == vettoreImgCaselle[c + 1]:
            GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
            disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
        if rx == vettoreImgCaselle[c] and ry == vettoreImgCaselle[c + 1]:
            GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
            disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
        for nemico in listaNemici:
            if not nemico.morto and nemico.inCasellaVista and nemico.x == vettoreImgCaselle[c] and nemico.y == vettoreImgCaselle[c + 1]:
                GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                break
        for personaggio in listaPersonaggi:
            if (personaggio.inCasellaVista or personaggio.mantieniSempreASchermo) and personaggio.x == vettoreImgCaselle[c] and personaggio.y == vettoreImgCaselle[c + 1]:
                GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                break
        c += 3

    # esche: id, vita, xesca, yesca
    i = 0
    while i < len(vettoreEsche):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                if primaDiAnima:
                    c = 0
                    while c < len(vettoreImgCaselle):
                        if vettoreEsche[i + 2] == vettoreImgCaselle[c] and vettoreEsche[i + 3] == vettoreImgCaselle[c + 1]:
                            GlobalVar.schermo.blit(vettoreImgCaselle[c + 2], (vettoreImgCaselle[c], vettoreImgCaselle[c + 1]))
                            disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[c], vettoreImgCaselle[c + 1], casellaChiara, casellaScura)
                            break
                        c += 3
                    GlobalVar.schermo.blit(GlobalVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                elif vettoreEsche[i + 1] > 0:
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
        i += 4

    # denaro: qta, x, y
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

    # robo (anche in caso di raffreddamento e autoricarica)
    if (raffreddamento and not primaDiAnima) or (raffredda > 0 and not raffreddamento):
        GlobalVar.schermo.blit(armrobS, (rx, ry))
        GlobalVar.schermo.blit(GlobalVar.robos, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == "raffred":
                imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
    elif (ricarica1 and not primaDiAnima) or (autoRic1 > 0 and not ricarica1):
        GlobalVar.schermo.blit(GlobalVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
    elif (ricarica2 and not primaDiAnima) or (autoRic2 > 0 and not ricarica2):
        GlobalVar.schermo.blit(GlobalVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == "ricarica+":
                imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
    else:
        GlobalVar.schermo.blit(robot, (rx, ry))
        if surrisc > 0:
            GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry))
        GlobalVar.schermo.blit(armrob, (rx, ry))

    disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

    # disegnare i nemici
    for nemico in listaNemici:
        if not nemico.morto and nemico.inCasellaVista:
            GlobalVar.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
            if nemico.avvelenato:
                GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
            if nemico.appiccicato:
                GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))

    # disegno tutti i personaggi
    for personaggio in listaPersonaggi:
        if personaggio.inCasellaVista or personaggio.mantieniSempreASchermo:
            GlobalVar.schermo.blit(personaggio.imgAttuale, (personaggio.x, personaggio.y))

    # backbround occhio/chiave
    GlobalVar.schermo.blit(GlobalVar.sfochiaveocchio, (GlobalVar.gsx - (GlobalVar.gpx * 5), 0))
    # vista nemici
    if apriocchio:
        GlobalVar.schermo.blit(GlobalVar.occhioape, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    else:
        GlobalVar.schermo.blit(GlobalVar.occhiochiu, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    # chiave robo
    if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
        if chiamarob:
            GlobalVar.schermo.blit(GlobalVar.chiaveroboacc, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))
        else:
            GlobalVar.schermo.blit(GlobalVar.chiaverobospe, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))

    # vita-status rallo
    lungvitatot = int(((GlobalVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalVar.indvita, (lungvitatot, GlobalVar.gpy // 4))
    fineindvitapers = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
    vitaral = pygame.transform.smoothscale(GlobalVar.vitapersonaggio, (lungvita, GlobalVar.gpy // 4))
    GlobalVar.schermo.blit(GlobalVar.sfondoRallo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(indvitapers, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(fineindvitapers, ((GlobalVar.gsx // 32 * 1) + lungvitatot, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(vitaral, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(GlobalVar.perss, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.perssb, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.imgNumFrecce, (int(GlobalVar.gsx // 32 * 1.2), GlobalVar.gsy // 18 * 17))
    messaggio(" x" + str(numFrecce), GlobalVar.grigiochi, int(GlobalVar.gsx // 32 * 1.8), int(GlobalVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 17))
    if attp > 0:
        GlobalVar.schermo.blit(GlobalVar.attaccopiu, (GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 17))
    if difp > 0:
        GlobalVar.schermo.blit(GlobalVar.difesapiu, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 17))

    # disegno la vita del mostro / Colco / esca selezionato
    if nemicoInquadrato == "Colco" or (not nemicoInquadrato and avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]):
        lungentot = int(((GlobalVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalVar.gpx * enrob) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalVar.indvita, (lungentot, GlobalVar.gpy // 4))
        fineindvitarob = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
        vitarob = pygame.transform.smoothscale(GlobalVar.vitarobo, (lungen, GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(GlobalVar.sfondoColco, (0, 0))
        GlobalVar.schermo.blit(indvitarob, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(fineindvitarob, (GlobalVar.gpx + lungentot, 0))
        GlobalVar.schermo.blit(vitarob, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(GlobalVar.robos, (0, 0))
        if surrisc > 0:
            GlobalVar.schermo.blit(GlobalVar.surriscaldato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if velp > 0:
            GlobalVar.schermo.blit(GlobalVar.velocitapiu, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if effp > 0:
            GlobalVar.schermo.blit(GlobalVar.efficienzapiu, ((GlobalVar.gpx * 3) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                pvEsca = vettoreEsche[i + 1]
                if primaDiAnima:
                    idEscaInizioturno = 0
                    j = 0
                    while j < len(statoEscheInizioTurno):
                        if statoEscheInizioTurno[j] == nemicoInquadrato:
                            idEscaInizioturno = j
                            break
                        j += 2
                    pvEsca = statoEscheInizioTurno[idEscaInizioturno + 1]
                lungvita = int(((GlobalVar.gpx * pvEsca) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalVar.schermo.blit(GlobalVar.sfondoEsche, (0, 0))
                GlobalVar.schermo.blit(GlobalVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (int(((GlobalVar.gpx * 1000) / float(4)) // 15), GlobalVar.gpy // 4))
                fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
                vitaesche = pygame.transform.smoothscale(GlobalVar.vitanemico0, (lungvita, GlobalVar.gpy // 4))
                GlobalVar.schermo.blit(indvitamost, (GlobalVar.gpx, 0))
                GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + int(((GlobalVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalVar.schermo.blit(vitaesche, (GlobalVar.gpx, 0))
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
        GlobalVar.schermo.blit(GlobalVar.sfondoMostro, (0, 0))
        if nemicoAvvelenato:
            GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if nemicoAppiccicato:
            GlobalVar.schermo.blit(GlobalVar.appiccicoso, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
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

    # disegno img GlobalVarG2.puntatoreInquadraNemici
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

    if not caricaTutto:
        if stanzaCambiata or uscitoDaMenu > 0:
            if uscitoDaMenu > 0:
                sprites = pygame.sprite.Group(Fade(1))
            else:
                sprites = pygame.sprite.Group(Fade(2))
            schermoFadeToBlack = GlobalVar.schermo.copy()
            i = 0
            while i <= 6:
                sprites.update()
                GlobalVar.schermo.blit(schermoFadeToBlack, (0, 0))
                sprites.draw(GlobalVar.schermo)
                pygame.display.update()
                GlobalVar.clockFadeToBlack.tick(GlobalVar.fpsFadeToBlack)
                i += 1
        else:
            pygame.display.update()


def analizzaColco(schermoBackground, casellaOscurata, x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, apriocchio, raffredda, autoRic1, autoRic2, mosseRimasteRob):
    if raffredda > 0 or autoRic1 > 0 or autoRic2 > 0 or mosseRimasteRob < 0:
        messaggioDiErrore = ""
        if raffredda > 0:
            messaggioDiErrore = "Raffreddamento in corso"
        elif autoRic1 > 0 or autoRic2 > 0:
            messaggioDiErrore = "Batteria in carica"
        elif mosseRimasteRob < 0:
            messaggioDiErrore = "Temperatura troppo elevata"
        vettorePrevisione = [["telecolco", messaggioDiErrore], [1, messaggioDiErrore], [2, messaggioDiErrore], [3, messaggioDiErrore], [4, messaggioDiErrore], [5, messaggioDiErrore], [6, messaggioDiErrore], [7, messaggioDiErrore], [8, messaggioDiErrore], [9, messaggioDiErrore], [10, messaggioDiErrore], ["ultimoObbiettivo", messaggioDiErrore]]
        previsionePosizioneObbiettivi = []
    else:
        vettorePrevisione, previsionePosizioneObbiettivi = movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco=True)

    GlobalVar.schermo.blit(schermoBackground, (0, 0))
    # background occhio/chiave
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

    i = 0
    while i < 32:
        j = 0
        while j < 18:
            casellaObbiettivo = False
            for casella in previsionePosizioneObbiettivi:
                if GlobalVar.gpx * i == casella[0] and GlobalVar.gpy * j == casella[1]:
                    casellaObbiettivo = True
                    break
            if not casellaObbiettivo:
                GlobalVar.schermo.blit(casellaOscurata, (GlobalVar.gpx * i, GlobalVar.gpy * j))
            j += 1
        i += 1

    if rx < GlobalVar.gsx // 32 * 16:
        xPartenzaPannello = GlobalVar.gsx // 32 * 19
    else:
        xPartenzaPannello = 0
    backgroundRiquadro = schermoBackground.subsurface(pygame.Rect(xPartenzaPannello, 0, GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 18))
    dark = pygame.Surface((GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 18), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 180))
    backgroundRiquadro.blit(dark, (0, 0))
    GlobalVar.schermo.blit(backgroundRiquadro, (xPartenzaPannello, 0))

    messaggio("Previsione prossima azione", GlobalVar.grigiochi, xPartenzaPannello + (GlobalVar.gsx // 32 * 1.5), GlobalVar.gsy // 18 * 1, 65)
    azionePrevistaTrovata = False
    messaggio("Movimento verso TeleColco", GlobalVar.grigiochi, xPartenzaPannello + (GlobalVar.gsx // 32 * 0.8), GlobalVar.gsy // 18 * 2.6, 40)
    if vettorePrevisione[0][1] == "":
        GlobalVar.schermo.blit(GlobalVar.puntatore, (xPartenzaPannello, GlobalVar.gsy // 18 * 2.5))
        messaggio("Istruzione eseguita salvo interferenza di Sara", GlobalVar.verde, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * 3.2, 35, daDestra=True)
        azionePrevistaTrovata = True
    else:
        messaggio(vettorePrevisione[0][1], GlobalVar.rosso, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * 3.2, 35, daDestra=True)
    # lista programmazione Colco
    c = 3.7
    for i in range(1, 11):
        if not azionePrevistaTrovata and vettorePrevisione[i][1] == "":
            GlobalVar.schermo.blit(GlobalVar.puntatore, (xPartenzaPannello, GlobalVar.gsy // 18 * c))
            messaggio("Istruzione eseguita salvo interferenza di Sara", GlobalVar.verde, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * (c + 0.6), 35, daDestra=True)
            azionePrevistaTrovata = True
        elif not azionePrevistaTrovata and vettorePrevisione[i][1] != "":
            messaggio(vettorePrevisione[i][1], GlobalVar.rosso, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * (c + 0.6), 35, daDestra=True)
        if i == 10:
            messaggio(str(i), GlobalVar.grigiochi, xPartenzaPannello + (GlobalVar.gsx // 32 * 0.7), GlobalVar.gsy // 18 * c, 50)
        else:
            messaggio(str(i), GlobalVar.grigiochi, xPartenzaPannello + (GlobalVar.gsx // 32 * 0.9), GlobalVar.gsy // 18 * c, 50)
        c += 1.1
    xListaCondizioni = xPartenzaPannello + (GlobalVar.gsx // 32 * 1.7)
    c = 3.8
    for i in range(101, 111):
        if dati[i] == -1:
            messaggio("---", GlobalVar.grigioscu, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 0:
            messaggio("---", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 1:
            messaggio("Sara con pv < 80%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 2:
            messaggio("Sara con pv < 50%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 3:
            messaggio("Sara con pv < 30%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 4:
            messaggio("Sara con veleno", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 5:
            messaggio("Colco surriscaldato", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 6:
            messaggio("Colco con pe < 80%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 7:
            messaggio("Colco con pe < 50%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 8:
            messaggio("Colco con pe < 30%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 9:
            messaggio("Sempre a Sara", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 10:
            messaggio("Sempre a Colco", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 11:
            messaggio("Nemico a caso", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 12:
            messaggio("Nemico vicino", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 13:
            messaggio("Nemico lontano", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 14:
            messaggio("Nemico con pv < 80%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 15:
            messaggio("Nemico con pv < 50%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 16:
            messaggio("Nemico con pv < 30%", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 17:
            messaggio("Nemico con meno pv", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 18:
            messaggio("Numero di nemici > 1", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 19:
            messaggio("Numero di nemici > 4", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 20:
            messaggio("Numero di nemici > 7", GlobalVar.grigiochi, xListaCondizioni, GlobalVar.gsy // 18 * c, 40)
        c += 1.1
    xListaTecniche = xPartenzaPannello + (GlobalVar.gsx // 32 * 7.2)
    c = 3.8
    for i in range(111, 121):
        if dati[i] == -1:
            messaggio("---", GlobalVar.grigioscu, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 0:
            messaggio("---", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 1:
            messaggio("Scossa", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 2:
            messaggio("Cura", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 3:
            messaggio("Antidoto", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 4:
            messaggio("Freccia elettrica", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 5:
            messaggio("Tempesta elettrica", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 6:
            messaggio("Raffreddamento", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 7:
            messaggio("Auto-ricarica", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 8:
            messaggio("Cura +", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 9:
            messaggio("Scossa +", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 10:
            messaggio("Freccia elettrica +", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 11:
            messaggio("Velocizza", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 12:
            messaggio("Carica attacco", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 13:
            messaggio("Carica difesa", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 14:
            messaggio("Efficienza", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 15:
            messaggio("Tempesta elettrica +", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 16:
            messaggio("Cura ++", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 17:
            messaggio("Auto-ricarica +", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 18:
            messaggio("Scossa ++", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 19:
            messaggio("Freccia Elettrica ++", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        if dati[i] == 20:
            messaggio("Tempesta elettrica ++", GlobalVar.grigiochi, xListaTecniche, GlobalVar.gsy // 18 * c, 40)
        c += 1.1
    messaggio("Movimento verso obbiettivo salvato in memoria", GlobalVar.grigiochi, xPartenzaPannello + (GlobalVar.gsx // 32 * 0.8), GlobalVar.gsy // 18 * 14.9, 40)
    if not azionePrevistaTrovata and vettorePrevisione[11][1] == "":
        GlobalVar.schermo.blit(GlobalVar.puntatore, (xPartenzaPannello, GlobalVar.gsy // 18 * 14.8))
        messaggio("Istruzione eseguita salvo interferenza di Sara", GlobalVar.verde, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * 15.5, 35, daDestra=True)
        azionePrevistaTrovata = True
    elif not azionePrevistaTrovata and vettorePrevisione[11][1] != "":
        messaggio(vettorePrevisione[11][1], GlobalVar.rosso, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * 15.5, 35, daDestra=True)
    messaggio("Nessuna azione da eseguire", GlobalVar.grigiochi, xPartenzaPannello + (GlobalVar.gsx // 32 * 0.8), GlobalVar.gsy // 18 * 16, 40)
    if not azionePrevistaTrovata:
        GlobalVar.schermo.blit(GlobalVar.puntatore, (xPartenzaPannello, GlobalVar.gsy // 18 * 15.9))
        messaggio("Istruzione eseguita salvo interferenza di Sara", GlobalVar.verde, xPartenzaPannello + (GlobalVar.gsx // 32 * 12.5), GlobalVar.gsy // 18 * 16.6, 35, daDestra=True)

    pygame.display.update()

    if not GlobalVar.mouseBloccato:
        GlobalVar.configuraCursore(True)
    risposta = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    mostraMouse = 2
    while not risposta:
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        mouseDaSpostare = False
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
            if mostraMouse == 0:
                GlobalVar.setCursoreVisibile(True)
                mostraMouse = 2
            else:
                mostraMouse -= 1
                mouseDaSpostare = True
        if mostraMouse == 1 and not mouseDaSpostare:
            mostraMouse = 2
        for event in pygame.event.get():
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
            if not sinistroMouseVecchio and sinistroMouse:
                centraleMouse = False
                destroMouse = False
            elif not centraleMouseVecchio and centraleMouse:
                sinistroMouse = False
                destroMouse = False
            elif not destroMouseVecchio and destroMouse:
                sinistroMouse = False
                centraleMouse = False
            if event.type == pygame.MOUSEBUTTONDOWN and not GlobalVar.mouseVisibile:
                GlobalVar.setCursoreVisibile(True)

            if event.type == pygame.QUIT:
                pygame.quit()
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                if GlobalVar.mouseVisibile:
                    GlobalVar.setCursoreVisibile(False)
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN:
                if destroMouse and not rotellaConCentralePremuto:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                else:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)


def attacca(dati, x, y, vx, vy, npers, nrob, rx, ry, obbiettivoCasualeColco, pers, pv, pvtot, difRallo, avvele, numCollanaIndossata, attp, difp, enrob, entot, difro, surrisc, velp, effp, stanzaa, casellaChiara, casellaScura, casellaOscurata, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, attVicino, attLontano, attacco, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, numFrecce, nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, avanzamentoStoria, casellePercorribili, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, mosseRimasteRob):
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
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                xp = vettoreEsche[i + 2]
                yp = vettoreEsche[i + 3]
                break
            i += 4

    attaccoDiRallo = [False, 0, False]
    xvp = xp
    yvp = yp
    nxp = 0
    nyp = 0
    risposta = False
    difesa = 0

    puntat = GlobalVar.puntatOut
    puntatogg = 0
    puntatogg1 = GlobalVar.puntatDif
    puntatogg2 = GlobalVar.puntatAtt
    puntatogg3 = GlobalVar.puntatPor
    puntatogg4 = GlobalVar.puntatAnalisi
    puntatogg5 = GlobalVar.puntatCof
    puntatogg6 = GlobalVar.puntatArc
    puntatogg7 = GlobalVar.puntatDialoghi

    # modifica puntatore a seconda dell'attacco
    if attacco == 1:
        puntatogg1 = GlobalVar.puntatDif
        puntatogg2 = GlobalVar.puntatAtt
        puntatogg3 = GlobalVar.puntatPor
        puntatogg4 = GlobalVar.puntatAnalisi
        puntatogg5 = GlobalVar.puntatCof
        puntatogg6 = GlobalVar.puntatArc
        puntatogg7 = GlobalVar.puntatDialoghi
    if attacco == 2:
        puntatogg = GlobalVar.puntatBom
    if attacco == 3:
        puntatogg = GlobalVar.puntatBoV
    if attacco == 4:
        puntatogg = GlobalVar.puntatEsc
    if attacco == 5:
        puntatogg = GlobalVar.puntatBoA
    if attacco == 6:
        puntatogg = GlobalVar.puntatBoP

    GlobalVar.schermo.blit(stanzaa, (0, 0))
    # salvo la lista di cofanetti vicini a ceselle viste per non mettergli la casella oscurata
    vetCofanettiVisti = []
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                vetCofanettiVisti.append(cofanetti[i + 1])
                vetCofanettiVisti.append(cofanetti[i + 2])
            j += 3
        i += 4
    # disegno l'ombreggiatura delle caselle
    i = 0
    while i < len(casellePercorribili):
        if casellePercorribili[i + 2]:
            if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 0:
                GlobalVar.schermo.blit(casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
            if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 1:
                GlobalVar.schermo.blit(casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
        else:
            casellaNonOscurata = False
            j = 0
            while j < len(vetCofanettiVisti):
                if casellePercorribili[i] == vetCofanettiVisti[j] and casellePercorribili[i + 1] == vetCofanettiVisti[j + 1]:
                    casellaNonOscurata = True
                j += 2
            if casellaNonOscurata:
                if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 0:
                    GlobalVar.schermo.blit(casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
                if ((casellePercorribili[i] / GlobalVar.gpx) + (casellePercorribili[i + 1] / GlobalVar.gpy)) % 2 == 1:
                    GlobalVar.schermo.blit(casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
            else:
                GlobalVar.schermo.blit(casellaOscurata, (casellePercorribili[i], casellePercorribili[i + 1]))
        i += 3

    # controllo caselle attaccabili tue e di Colco
    raggioDiLancio = 0
    caseattactot = []
    if attacco == 1:
        caseattactot = trovacasattaccabili(x, y, -1, caseviste)
    if attacco == 2:
        caseattactot = trovacasattaccabili(x, y, GlobalVar.gpx * 6, caseviste)
        raggioDiLancio = 6
    if attacco == 3:
        caseattactot = trovacasattaccabili(x, y, GlobalVar.gpx * 5, caseviste)
        raggioDiLancio = 5
    if attacco == 4:
        caseattactot = trovacasattaccabili(x, y, GlobalVar.gpx * 6, caseviste)
        raggioDiLancio = 6
    if attacco == 5:
        caseattactot = trovacasattaccabili(x, y, GlobalVar.gpx * 5, caseviste)
        raggioDiLancio = 5
    if attacco == 6:
        caseattactot = trovacasattaccabili(x, y, GlobalVar.gpx * 4, caseviste)
        raggioDiLancio = 4
    if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and (posizioneColcoAggiornamentoCaseAttac[0] != rx or posizioneColcoAggiornamentoCaseAttac[1] != ry):
        caselleAttaccabiliColco = trovacasattaccabili(rx, ry, GlobalVar.vistaRobo * GlobalVar.gpx, caseviste)
        posizioneColcoAggiornamentoCaseAttac = [rx, ry]

    listaNemiciVisti = []
    for nemico in listaNemici:
        if nemico.inCasellaVista:
            listaNemiciVisti.append(nemico)

    # disegna porte
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
        i += 4
    # disegna cofanetti
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                if cofanetti[i + 3]:
                    GlobalVar.schermo.blit(GlobalVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    GlobalVar.schermo.blit(GlobalVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
            j += 3
        i += 4

    # esche: id, vita, xesca, yesca
    i = 0
    while i < len(vettoreEsche):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == vettoreEsche[i + 2] - GlobalVar.gpx and caseviste[j + 1] == vettoreEsche[i + 3]) or (caseviste[j] == vettoreEsche[i + 2] + GlobalVar.gpx and caseviste[j + 1] == vettoreEsche[i + 3]) or (caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] - GlobalVar.gpy) or (caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] + GlobalVar.gpy)) and caseviste[j + 2]:
                GlobalVar.schermo.blit(GlobalVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            j += 3
        i += 4

    # denaro: qta, x, y
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == vettoreDenaro[i + 1] - GlobalVar.gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] + GlobalVar.gpx and caseviste[j + 1] == vettoreDenaro[i + 2]) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] - GlobalVar.gpy) or (caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2] + GlobalVar.gpy)) and caseviste[j + 2]:
                GlobalVar.schermo.blit(GlobalVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3

    # robo (anche in caso di raffreddamento e autoricarica)
    if raffredda > 0:
        GlobalVar.schermo.blit(armrobS, (rx, ry))
        GlobalVar.schermo.blit(GlobalVar.robos, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == "raffred":
                imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
    elif autoRic1 > 0:
        GlobalVar.schermo.blit(GlobalVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
    elif autoRic2 > 0:
        GlobalVar.schermo.blit(GlobalVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalVar.vetAnimazioniTecniche):
            if GlobalVar.vetAnimazioniTecniche[i] == "ricarica+":
                imgAnimazione = GlobalVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalVar.schermo.blit(imgAnimazione, (rx, ry))
    else:
        GlobalVar.schermo.blit(robot, (rx, ry))
        if surrisc > 0:
            GlobalVar.schermo.blit(GlobalVar.roboSurrisc, (rx, ry))
        GlobalVar.schermo.blit(armrob, (rx, ry))

    # personaggio
    disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

    # disegnare i mostri
    for nemico in listaNemici:
        if nemico.inCasellaVista:
            GlobalVar.schermo.blit(nemico.imgAttuale, (nemico.x, nemico.y))
            if nemico.avvelenato:
                GlobalVar.schermo.blit(nemico.imgAvvelenamento, (nemico.x, nemico.y))
            if nemico.appiccicato:
                GlobalVar.schermo.blit(nemico.imgAppiccicato, (nemico.x, nemico.y))

    # disegno tutti i personaggi
    for personaggio in listaPersonaggi:
        if (personaggio.mantieniSempreASchermo and personaggio.vicinoACasellaVista) or personaggio.inCasellaVista:
            GlobalVar.schermo.blit(personaggio.imgAttuale, (personaggio.x, personaggio.y))

    # vita nemico selezionato
    if not type(nemicoInquadrato) is str and nemicoInquadrato:
        pvm = nemicoInquadrato.vita
        pvmtot = nemicoInquadrato.vitaTotale
        GlobalVar.schermo.blit(GlobalVar.sfondoMostro, (0, 0))
        if nemicoInquadrato.avvelenato:
            GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if nemicoInquadrato.appiccicato:
            GlobalVar.schermo.blit(GlobalVar.appiccicoso, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
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
    # vita esca selezionata
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                lungvita = int(((GlobalVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalVar.schermo.blit(GlobalVar.sfondoEsche, (0, 0))
                GlobalVar.schermo.blit(GlobalVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (int(((GlobalVar.gpx * 1000) / float(4)) // 15), GlobalVar.gpy // 4))
                fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
                vitaesche = pygame.transform.smoothscale(GlobalVar.vitanemico0, (lungvita, GlobalVar.gpy // 4))
                GlobalVar.schermo.blit(indvitamost, (GlobalVar.gpx, 0))
                GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + int(((GlobalVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalVar.schermo.blit(vitaesche, (GlobalVar.gpx, 0))
                break
            i += 4
    # altrimenti mostro solo la vita di colco
    elif avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
        lungentot = int(((GlobalVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalVar.gpx * enrob) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalVar.indvita, (lungentot, GlobalVar.gpy // 4))
        fineindvitarob = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
        vitarob = pygame.transform.smoothscale(GlobalVar.vitarobo, (lungen, GlobalVar.gpy // 4))
        GlobalVar.schermo.blit(GlobalVar.sfondoColco, (0, 0))
        GlobalVar.schermo.blit(indvitarob, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(fineindvitarob, (GlobalVar.gpx + lungentot, 0))
        GlobalVar.schermo.blit(vitarob, (GlobalVar.gpx, 0))
        GlobalVar.schermo.blit(GlobalVar.robos, (0, 0))
        if surrisc > 0:
            GlobalVar.schermo.blit(GlobalVar.surriscaldato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if velp > 0:
            GlobalVar.schermo.blit(GlobalVar.velocitapiu, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        if effp > 0:
            GlobalVar.schermo.blit(GlobalVar.efficienzapiu, ((GlobalVar.gpx * 3) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))

    # background occhio/chiave
    GlobalVar.schermo.blit(GlobalVar.sfochiaveocchio, (GlobalVar.gsx - (GlobalVar.gpx * 5), 0))
    # vista nemici
    if apriocchio:
        GlobalVar.schermo.blit(GlobalVar.occhioape, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    else:
        GlobalVar.schermo.blit(GlobalVar.occhiochiu, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
    # chiave robo
    if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
        if chiamarob:
            GlobalVar.schermo.blit(GlobalVar.chiaveroboacc, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))
        else:
            GlobalVar.schermo.blit(GlobalVar.chiaverobospe, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))

    # vita-status rallo
    lungvitatot = int(((GlobalVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalVar.indvita, (lungvitatot, GlobalVar.gpy // 4))
    fineindvitapers = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
    vitaral = pygame.transform.smoothscale(GlobalVar.vitapersonaggio, (lungvita, GlobalVar.gpy // 4))
    GlobalVar.schermo.blit(GlobalVar.sfondoRallo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(indvitapers, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(fineindvitapers, ((GlobalVar.gsx // 32 * 1) + lungvitatot, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(vitaral, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(GlobalVar.perss, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.perssb, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.imgNumFrecce, (int(GlobalVar.gsx // 32 * 1.2), GlobalVar.gsy // 18 * 17))
    messaggio(" x" + str(numFrecce), GlobalVar.grigiochi, int(GlobalVar.gsx // 32 * 1.8), int(GlobalVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 17))
    if attp > 0:
        GlobalVar.schermo.blit(GlobalVar.attaccopiu, (GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 17))
    if difp > 0:
        GlobalVar.schermo.blit(GlobalVar.difesapiu, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 17))

    schermoPrevisioneColco = GlobalVar.schermo.copy()

    # disegno le caselle non attaccabili (prima cerco gli oggetti che hanno accanto una casellaAttaccabile per non oscurarli)
    vetCaselleDaNonOscurare = []
    i = 0
    while i < len(caseattactot):
        if caseattactot[i + 2] or (caseattactot[i] == x and caseattactot[i + 1] == y):
            j = 0
            while j < len(porte):
                if not porte[j + 3]:
                    if (caseattactot[i] == porte[j + 1] - GlobalVar.gpx and caseattactot[i + 1] == porte[j + 2]) or (caseattactot[i] == porte[j + 1] + GlobalVar.gpx and caseattactot[i + 1] == porte[j + 2]) or (caseattactot[i] == porte[j + 1] and caseattactot[i + 1] == porte[j + 2] - GlobalVar.gpy) or (caseattactot[i] == porte[j + 1] and caseattactot[i + 1] == porte[j + 2] + GlobalVar.gpy):
                        vetCaselleDaNonOscurare.append(porte[j + 1])
                        vetCaselleDaNonOscurare.append(porte[j + 2])
                j += 4
            j = 0
            while j < len(cofanetti):
                if (caseattactot[i] == cofanetti[j + 1] - GlobalVar.gpx and caseattactot[i + 1] == cofanetti[j + 2]) or (caseattactot[i] == cofanetti[j + 1] + GlobalVar.gpx and caseattactot[i + 1] == cofanetti[j + 2]) or (caseattactot[i] == cofanetti[j + 1] and caseattactot[i + 1] == cofanetti[j + 2] - GlobalVar.gpy) or (caseattactot[i] == cofanetti[j + 1] and caseattactot[i + 1] == cofanetti[j + 2] + GlobalVar.gpy):
                    vetCaselleDaNonOscurare.append(cofanetti[j + 1])
                    vetCaselleDaNonOscurare.append(cofanetti[j + 2])
                j += 4
            for personaggio in listaPersonaggi:
                if personaggio.mantieniSempreASchermo and personaggio.vicinoACasellaVista:
                    if (caseattactot[i] == personaggio.x - GlobalVar.gpx and caseattactot[i + 1] == personaggio.y) or (caseattactot[i] == personaggio.x + GlobalVar.gpx and caseattactot[i + 1] == personaggio.y) or (caseattactot[i] == personaggio.x and caseattactot[i + 1] == personaggio.y - GlobalVar.gpy) or (caseattactot[i] == personaggio.x and caseattactot[i + 1] == personaggio.y + GlobalVar.gpy):
                        vetCaselleDaNonOscurare.append(personaggio.x)
                        vetCaselleDaNonOscurare.append(personaggio.y)
        i += 3
    i = 0
    while i < len(caseattactot):
        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
            casellaDaOscurare = True
            j = 0
            while j < len(vetCaselleDaNonOscurare):
                if caseattactot[i] == vetCaselleDaNonOscurare[j] and caseattactot[i + 1] == vetCaselleDaNonOscurare[j + 1]:
                    casellaDaOscurare = False
                    break
                j += 2
            if casellaDaOscurare:
                GlobalVar.schermo.blit(GlobalVar.caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
        i += 3

    # vita-status rallo => la ridisegno perché viene oscurata in quanto si trova in caselle non viste
    lungvitatot = int(((GlobalVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalVar.indvita, (lungvitatot, GlobalVar.gpy // 4))
    fineindvitapers = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
    vitaral = pygame.transform.smoothscale(GlobalVar.vitapersonaggio, (lungvita, GlobalVar.gpy // 4))
    GlobalVar.schermo.blit(GlobalVar.sfondoRallo, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(indvitapers, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(fineindvitapers, ((GlobalVar.gsx // 32 * 1) + lungvitatot, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(vitaral, (GlobalVar.gsx // 32 * 1, (GlobalVar.gsy // 18 * 17) + (GlobalVar.gpy // 4 * 3)))
    GlobalVar.schermo.blit(GlobalVar.perss, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.perssb, (GlobalVar.gsx // 32 * 0, GlobalVar.gsy // 18 * 17))
    GlobalVar.schermo.blit(GlobalVar.imgNumFrecce, (int(GlobalVar.gsx // 32 * 1.2), GlobalVar.gsy // 18 * 17))
    messaggio(" x" + str(numFrecce), GlobalVar.grigiochi, int(GlobalVar.gsx // 32 * 1.8), int(GlobalVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 17))
    if attp > 0:
        GlobalVar.schermo.blit(GlobalVar.attaccopiu, (GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 17))
    if difp > 0:
        GlobalVar.schermo.blit(GlobalVar.difesapiu, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 17))

    schermoOriginale = GlobalVar.schermo.copy()

    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
    mostraMouse = 2
    tastotempfps = 4
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
    analisiDiColcoEffettuata = False
    puntaPorta = False
    attaccato = False
    attaccoADistanza = False
    sposta = False
    interagisciConPersonaggio = False
    interazioneConfermata = False
    primoFrame = True
    vecchiaCasellaInquadrata = [False, 0, 0]

    while not risposta:
        if xp != xvp or yp != yvp:
            appenaCaricato = False
        xvp = xp
        yvp = yp

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps -= 1
            nxp = 0
            nyp = 0
        if tastotempfps == 0 and tastop != 0:
            if tastop == pygame.K_w:
                nyp = -GlobalVar.gpy
            if tastop == pygame.K_a:
                nxp = -GlobalVar.gpx
            if tastop == pygame.K_s:
                nyp = GlobalVar.gpy
            if tastop == pygame.K_d:
                nxp = GlobalVar.gpx
            tastotempfps = 2
            xvp = xp
            yvp = yp

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        mouseDaSpostare = False
        if deltaXMouse != 0 or deltaYMouse != 0 or (primoFrame and GlobalVar.mouseVisibile) or (analisiDiColcoEffettuata and GlobalVar.mouseVisibile):
            if not GlobalVar.mouseVisibile:
                if mostraMouse == 0:
                    GlobalVar.setCursoreVisibile(True)
                    mostraMouse = 2
                else:
                    mostraMouse -= 1
                    mouseDaSpostare = True
            casellaTrovata = False
            i = 0
            while i < len(caseviste):
                if caseviste[i] < xMouse < caseviste[i] + GlobalVar.gpx and caseviste[i + 1] < yMouse < caseviste[i + 1] + GlobalVar.gpy and caseviste[i + 2]:
                    if xp != caseviste[i] or yp != caseviste[i + 1]:
                        if not primoFrame:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = xMouse - (xMouse % GlobalVar.gpx)
                        yp = yMouse - (yMouse % GlobalVar.gpy)
                    casellaTrovata = True
                    break
                i += 3
            if not casellaTrovata:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i + 1] < xMouse < cofanetti[i + 1] + GlobalVar.gpx and cofanetti[i + 2] < yMouse < cofanetti[i + 2] + GlobalVar.gpy:
                        if xp != cofanetti[i + 1] or yp != cofanetti[i + 2]:
                            j = 0
                            while j < len(caseviste):
                                if ((cofanetti[i + 1] + GlobalVar.gpx == caseviste[j] and cofanetti[i + 2] == caseviste[j + 1]) or (cofanetti[i + 1] - GlobalVar.gpx == caseviste[j] and cofanetti[i + 2] == caseviste[j + 1]) or (cofanetti[i + 1] == caseviste[j] and cofanetti[i + 2] + GlobalVar.gpy == caseviste[j + 1]) or (cofanetti[i + 1] == caseviste[j] and cofanetti[i + 2] - GlobalVar.gpy == caseviste[j + 1])) and caseviste[j + 2]:
                                    if not primoFrame:
                                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                                    xp = xMouse - (xMouse % GlobalVar.gpx)
                                    yp = yMouse - (yMouse % GlobalVar.gpy)
                                    break
                                j += 3
                        casellaTrovata = True
                        break
                    i += 4
            if not casellaTrovata:
                i = 0
                while i < len(porte):
                    if porte[i + 1] < xMouse < porte[i + 1] + GlobalVar.gpx and porte[i + 2] < yMouse < porte[i + 2] + GlobalVar.gpy:
                        if xp != porte[i + 1] or yp != porte[i + 2]:
                            j = 0
                            while j < len(caseviste):
                                if ((porte[i + 1] + GlobalVar.gpx == caseviste[j] and porte[i + 2] == caseviste[j + 1]) or (porte[i + 1] - GlobalVar.gpx == caseviste[j] and porte[i + 2] == caseviste[j + 1]) or (porte[i + 1] == caseviste[j] and porte[i + 2] + GlobalVar.gpy == caseviste[j + 1]) or (porte[i + 1] == caseviste[j] and porte[i + 2] - GlobalVar.gpy == caseviste[j + 1])) and caseviste[j + 2]:
                                    puntaPorta = True
                                    if not primoFrame:
                                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                                    xp = xMouse - (xMouse % GlobalVar.gpx)
                                    yp = yMouse - (yMouse % GlobalVar.gpy)
                                    break
                                j += 3
                        casellaTrovata = True
                        break
                    i += 4
            if not casellaTrovata:
                for personaggioOggetto in listaPersonaggi:
                    if personaggioOggetto.mantieniSempreASchermo and personaggioOggetto.x < xMouse < personaggioOggetto.x + GlobalVar.gpx and personaggioOggetto.y < yMouse < personaggioOggetto.y + GlobalVar.gpy:
                        if personaggioOggetto.vicinoACasellaVista and (xp != personaggioOggetto.x or yp != personaggioOggetto.y):
                            if not primoFrame:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                            xp = xMouse - (xMouse % GlobalVar.gpx)
                            yp = yMouse - (yMouse % GlobalVar.gpy)
                        casellaTrovata = True
                        break
        if mostraMouse == 1 and not mouseDaSpostare:
            mostraMouse = 2
        if GlobalVar.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / Rallo / Colco / personaggio / porta / cofanetto / nemico / casella nel raggio (in caso di oggetto)
            if GlobalVar.gsy // 18 * 17 <= yMouse <= GlobalVar.gsy and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 6:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"])) and 0 <= yMouse <= GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 <= xMouse <= GlobalVar.gsx // 32 * 4:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 < yMouse < GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 < xMouse < GlobalVar.gsx // 32 * 1:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 < yMouse < GlobalVar.gsy // 18 * 1 and GlobalVar.gsx // 32 * 0 < xMouse < GlobalVar.gsx // 32 * 3:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and 0 <= yMouse <= GlobalVar.gsy // 18 * 1.5 and GlobalVar.gsx // 32 * 27.8 < xMouse <= GlobalVar.gsx // 32 * 30.2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            elif y < yMouse < y + GlobalVar.gpy and x < xMouse < x + GlobalVar.gpx:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "Rallo"
            elif ry < yMouse < ry + GlobalVar.gpy and rx < xMouse < rx + GlobalVar.gpx:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                inquadratoQualcosa = "Colco"
            else:
                if not inquadratoQualcosa:
                    for personaggio in listaPersonaggi:
                        if personaggio.x < xMouse < personaggio.x + GlobalVar.gpx and personaggio.y < yMouse < personaggio.y + GlobalVar.gpy:
                            if (personaggio.x == x + GlobalVar.gpx and personaggio.y == y) or (personaggio.x == x - GlobalVar.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalVar.gpy) or (personaggio.x == x and personaggio.y == y - GlobalVar.gpy):
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "personaggio"
                            break
                if not inquadratoQualcosa:
                    for nemico in listaNemiciVisti:
                        if nemico.x < xMouse < nemico.x + GlobalVar.gpx and nemico.y < yMouse < nemico.y + GlobalVar.gpy:
                            if nemicoInquadrato and type(nemicoInquadrato) is not str and nemico.x == nemicoInquadrato.x and nemico.y == nemicoInquadrato.y:
                                j = 0
                                while j < len(caseattactot):
                                    if caseattactot[j] == nemico.x and caseattactot[j + 1] == nemico.y:
                                        if caseattactot[j + 2] and ((abs(nemico.x - x) <= GlobalVar.gpx and abs(nemico.y - y) <= GlobalVar.gpy and not abs(nemico.x - x) == abs(nemico.y - y)) or numFrecce > 0):
                                            if GlobalVar.mouseBloccato:
                                                GlobalVar.configuraCursore(False)
                                            inquadratoQualcosa = "nemico"
                                        break
                                    j += 3
                            elif nemico.inCasellaVista:
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "nemico"
                            break
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] < xMouse < porte[i + 1] + GlobalVar.gpx and porte[i + 2] < yMouse < porte[i + 2] + GlobalVar.gpy:
                            if (porte[i + 1] == x + GlobalVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalVar.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalVar.gpy):
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "porta"
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] < xMouse < cofanetti[i + 1] + GlobalVar.gpx and cofanetti[i + 2] < yMouse < cofanetti[i + 2] + GlobalVar.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalVar.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalVar.gpy)) and not cofanetti[i + 3]:
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto"
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(vettoreEsche):
                        if vettoreEsche[i + 2] < xMouse < vettoreEsche[i + 2] + GlobalVar.gpx and vettoreEsche[i + 3] < yMouse < vettoreEsche[i + 3] + GlobalVar.gpy:
                            if nemicoInquadrato and type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                                idEscaInquadrata = int(nemicoInquadrato[4:])
                                if idEscaInquadrata == vettoreEsche[i]:
                                    j = 0
                                    while j < len(caseattactot):
                                        if caseattactot[j] == vettoreEsche[i + 2] and caseattactot[j + 1] == vettoreEsche[i + 3]:
                                            if caseattactot[j + 2] and ((abs(vettoreEsche[i + 2] - x) <= GlobalVar.gpx and abs(vettoreEsche[i + 3] - y) <= GlobalVar.gpy and not abs(vettoreEsche[i + 2] - x) == abs(vettoreEsche[i + 3] - y)) or numFrecce > 0):
                                                if GlobalVar.mouseBloccato:
                                                    GlobalVar.configuraCursore(False)
                                                inquadratoQualcosa = "esca"
                                            break
                                        j += 3
                                else:
                                    if GlobalVar.mouseBloccato:
                                        GlobalVar.configuraCursore(False)
                                    inquadratoQualcosa = "esca"
                            else:
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "esca"
                            break
                        i += 4
                if not inquadratoQualcosa and attacco > 1:
                    if x - GlobalVar.gpx * raggioDiLancio <= xMouse <= x + GlobalVar.gpx + GlobalVar.gpx * raggioDiLancio and y - GlobalVar.gpy * raggioDiLancio <= yMouse <= y + GlobalVar.gpy + GlobalVar.gpy * raggioDiLancio:
                        i = 0
                        while i < len(caseattactot):
                            if caseattactot[i] <= xMouse <= caseattactot[i] + GlobalVar.gpx and caseattactot[i + 1] <= yMouse <= caseattactot[i + 1] + GlobalVar.gpy and caseattactot[i + 2]:
                                if GlobalVar.mouseBloccato:
                                    GlobalVar.configuraCursore(False)
                                inquadratoQualcosa = "casellaNelRaggio"
                                break
                            i += 3
        if not inquadratoQualcosa:
            if not GlobalVar.mouseBloccato:
                GlobalVar.configuraCursore(True)
        primoFrame = False

        for event in pygame.event.get():
            tastotempfps = 4
            sinistroMouseVecchio = sinistroMouse
            centraleMouseVecchio = centraleMouse
            destroMouseVecchio = destroMouse
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            rotellaConCentralePremuto = False
            if centraleMouseVecchio and centraleMouse:
                rotellaConCentralePremuto = True
            if not sinistroMouseVecchio and sinistroMouse:
                centraleMouse = False
                destroMouse = False
            elif not centraleMouseVecchio and centraleMouse:
                sinistroMouse = False
                destroMouse = False
            elif not destroMouseVecchio and destroMouse:
                sinistroMouse = False
                centraleMouse = False
            if event.type == pygame.MOUSEBUTTONDOWN and not GlobalVar.mouseVisibile:
                GlobalVar.setCursoreVisibile(True)

            if event.type == pygame.QUIT:
                pygame.quit()
                GlobalVar.quit()
            if event.type == pygame.KEYDOWN:
                tastop = event.key

                if GlobalVar.mouseVisibile:
                    GlobalVar.setCursoreVisibile(False)
                # esci
                if event.key == pygame.K_q:
                    risposta = True
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                # esci e apri il menu
                if event.key == pygame.K_ESCAPE:
                    risposta = True
                    startf = True

                # attiva / disattiva il gambit
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoTeleColco)
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
                    # seleziono i nemici / esche visti/e + controllo se il puntatore è su un nemico / esca / Colco
                    listaNemiciVisti = []
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            listaNemiciVisti.append(nemico)
                            if nemico.x == xp and nemico.y == yp:
                                nemicoInquadratoTemp = nemico
                    listaEscheViste = []
                    i = 0
                    while i < len(vettoreEsche):
                        j = 0
                        while j < len(caseviste):
                            if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                                listaEscheViste.append(vettoreEsche[i])
                                listaEscheViste.append(vettoreEsche[i + 1])
                                listaEscheViste.append(vettoreEsche[i + 2])
                                listaEscheViste.append(vettoreEsche[i + 3])
                                if vettoreEsche[i + 2] == xp and vettoreEsche[i + 3] == yp:
                                    nemicoInquadratoTemp = "Esca" + str(vettoreEsche[i])
                            j += 3
                        i += 4
                    if rx == xp and ry == yp:
                        nemicoInquadratoTemp = "Colco"
                    nemicoInquadratoTemp = scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadratoTemp, listaNemiciVisti, listaEscheViste, True)

                    if not nemicoInquadratoTemp:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp == "Colco":
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = rx
                        yp = ry
                    elif not type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = nemicoInquadratoTemp.x
                        yp = nemicoInquadratoTemp.y
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 2]
                        yp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 3]
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    nemicoInquadratoTemp = False
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    # seleziono i nemici / esche visti/e + controllo se il puntatore è su un nemico / esca / Colco
                    listaNemiciVisti = []
                    for nemico in listaNemici:
                        if nemico.inCasellaVista:
                            listaNemiciVisti.append(nemico)
                            if nemico.x == xp and nemico.y == yp:
                                nemicoInquadratoTemp = nemico
                    listaEscheViste = []
                    i = 0
                    while i < len(vettoreEsche):
                        j = 0
                        while j < len(caseviste):
                            if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                                listaEscheViste.append(vettoreEsche[i])
                                listaEscheViste.append(vettoreEsche[i + 1])
                                listaEscheViste.append(vettoreEsche[i + 2])
                                listaEscheViste.append(vettoreEsche[i + 3])
                                if vettoreEsche[i + 2] == xp and vettoreEsche[i + 3] == yp:
                                    nemicoInquadratoTemp = "Esca" + str(vettoreEsche[i])
                            j += 3
                        i += 4
                    if rx == xp and ry == yp:
                        nemicoInquadratoTemp = "Colco"
                    nemicoInquadratoTemp = scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadratoTemp, listaNemiciVisti, listaEscheViste, False)

                    if not nemicoInquadratoTemp:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp == "Colco":
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = rx
                        yp = ry
                    elif not type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = nemicoInquadratoTemp.x
                        yp = nemicoInquadratoTemp.y
                    elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                        xp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 2]
                        yp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 3]

                if event.key == pygame.K_e:
                    selezioneAvvenuta = False
                    if xp == rx and yp == ry:
                        selezioneAvvenuta = True
                        nemicoInquadrato = "Colco"
                    else:
                        i = 0
                        while i < len(vettoreEsche):
                            if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                                nemicoInquadrato = "Esca" + str(vettoreEsche[i])
                                selezioneAvvenuta = True
                            i += 4
                        if not selezioneAvvenuta:
                            for nemico in listaNemici:
                                if xp == nemico.x and yp == nemico.y:
                                    nemicoInquadrato = nemico
                                    selezioneAvvenuta = True
                    if selezioneAvvenuta:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
                    else:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)

                # movimento puntatore
                if event.key == pygame.K_w:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nyp = -GlobalVar.gpy
                    nxp = 0
                if event.key == pygame.K_a:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nxp = -GlobalVar.gpx
                    nyp = 0
                if event.key == pygame.K_s:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nyp = GlobalVar.gpy
                    nxp = 0
                if event.key == pygame.K_d:
                    suPorta = False
                    suCofanetto = False
                    numTastiPremuti += 1
                    nxp = GlobalVar.gpx
                    nyp = 0
                # attacco
                if event.key == pygame.K_SPACE:
                    interazioneConfermata = True

            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse and not rotellaConCentralePremuto and not startf:
                tastop = "mouseDestro"
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                risposta = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and centraleMouse and not rotellaConCentralePremuto and not startf:
                tastop = "mouseCentrale"
                risposta = True
                startf = True
            if GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and not GlobalVar.mouseBloccato and not startf:
                tastop = "mouseSinistro"
                if inquadratoQualcosa == "start":
                    risposta = True
                    startf = True
                elif inquadratoQualcosa == "battaglia":
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    risposta = True
                elif inquadratoQualcosa == "telecolco":
                    GlobalVar.canaleSoundInterazioni.play(GlobalVar.suonoTeleColco)
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                elif inquadratoQualcosa == "Rallo":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "Colco":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "porta":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "cofanetto":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "personaggio":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "nemico":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "esca":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "casellaNelRaggio":
                    interazioneConfermata = True
            elif GlobalVar.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not rotellaConCentralePremuto and GlobalVar.mouseBloccato:
                GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)
            if event.type == pygame.KEYUP:
                if tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d:
                    numTastiPremuti -= 1
                    if event.key == tastop:
                        numTastiPremuti = 0
                else:
                    numTastiPremuti = 0
                if numTastiPremuti == 0:
                    tastop = 0
                    nxp = 0
                    nyp = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        analisiDiColcoEffettuata = False
        if interazioneConfermata:
            interazioneConfermata = False
            daInquadrare = False
            if tastop == "mouseSinistro" and (inquadratoQualcosa == "nemico" or inquadratoQualcosa == "esca" or inquadratoQualcosa == "Colco"):
                if inquadratoQualcosa == "nemico" and not (nemicoInquadrato and type(nemicoInquadrato) is not str and xp == nemicoInquadrato.x and yp == nemicoInquadrato.y):
                    for nemico in listaNemici:
                        if xp == nemico.x and yp == nemico.y:
                            GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
                            nemicoInquadrato = nemico
                            daInquadrare = True
                            break
                if inquadratoQualcosa == "esca":
                    if not (nemicoInquadrato and type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca")):
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
                        i = 0
                        while i < len(vettoreEsche):
                            if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                                nemicoInquadrato = "Esca" + str(vettoreEsche[i])
                                break
                            i += 4
                        daInquadrare = True
                    else:
                        idEscaInquadrata = int(nemicoInquadrato[4:])
                        i = 0
                        while i < len(vettoreEsche):
                            if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                                if not idEscaInquadrata == vettoreEsche[i]:
                                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
                                    nemicoInquadrato = "Esca" + str(vettoreEsche[i])
                                    daInquadrare = True
                                break
                            i += 4
                if inquadratoQualcosa == "Colco" and not (type(nemicoInquadrato) is str and nemicoInquadrato == "Colco"):
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selObbiettivo)
                    nemicoInquadrato = "Colco"
                    daInquadrare = True
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
                if attacco == 1 and ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)) and suPersonaggio:
                    interagisciConPersonaggio = True
                    risposta = True
                    if xp == x + GlobalVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVar.gpy:
                        npers = 3
                # analizza Colco attacco = 1
                elif attacco == 1 and (xp == rx and yp == ry) and not (rx == x and ry == y):
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selezione)
                    analizzaColco(copy.copy(schermoPrevisioneColco), casellaOscurata, x, y, vx, vy, rx, ry, chiamarob, dati[:], porte[:], copy.deepcopy(listaNemici), difesa, ultimoObbiettivoColco[:], copy.deepcopy(obbiettivoCasualeColco), copy.deepcopy(listaPersonaggi), caseviste[:], caselleAttaccabiliColco[:], posizioneColcoAggiornamentoCaseAttac[:], vettoreEsche[:], apriocchio, raffredda, autoRic1, autoRic2, mosseRimasteRob)
                    analisiDiColcoEffettuata = True
                    GlobalVar.schermo.blit(schermoOriginale, (0, 0))
                # apri/chiudi porta attacco = 1
                elif attacco == 1 and ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)) and suPorta:
                    apriChiudiPorta = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVar.gpy:
                        npers = 3
                # apri cofanetto attacco = 1
                elif attacco == 1 and ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)) and suCofanetto:
                    apriCofanetto = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVar.gpy:
                        npers = 3
                # attacco ravvicinato attacco = 1
                elif attacco == 1 and ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)):
                    infliggidanno = True
                    danno = attVicino
                    raggio = GlobalVar.gpx * 0
                # attacco lontano attacco = 1
                elif attacco == 1 and not ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy) or (xp == x and yp == y) or (xp == rx and yp == ry)) and numFrecce > 0:
                    j = 0
                    while j < len(caseattactot):
                        if caseattactot[j] == xp and caseattactot[j + 1] == yp:
                            if caseattactot[j + 2]:
                                infliggidanno = True
                                danno = attLontano
                                raggio = GlobalVar.gpx * 0
                            break
                        j += 3
                # difesa attacco = 1
                elif attacco == 1 and (xp == x and yp == y):
                    difesa = 2
                    risposta = True
                # bomba attacco = 2
                if attacco == 2 and (abs(x - xp) <= GlobalVar.gpx * 6 and abs(y - yp) <= GlobalVar.gpy * 6):
                    # controllo caselle attaccabili
                    continua = True
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                                continua = False
                            break
                        i += 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) == abs(yp - y) == 0:
                            npers = 3
                        elif abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
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
                        danno = GlobalVar.dannoOggetti[0]
                        raggio = GlobalVar.gpx * 1
                        sposta = True
                        risposta = True
                # bomba veleno attacco = 3
                if attacco == 3 and (abs(x - xp) <= GlobalVar.gpx * 5 and abs(y - yp) <= GlobalVar.gpy * 5):
                    # controllo caselle attaccabili
                    continua = True
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                                continua = False
                            break
                        i += 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) == abs(yp - y) == 0:
                            npers = 3
                        elif abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
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
                        danno = GlobalVar.dannoOggetti[1]
                        statom = 1
                        raggio = GlobalVar.gpx * 0
                        sposta = True
                        risposta = True
                # esca attacco = 4
                if attacco == 4 and (abs(x - xp) <= GlobalVar.gpx * 6 and abs(y - yp) <= GlobalVar.gpy * 6):
                    # controllo caselle attaccabili
                    continua = True
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                                continua = False
                            break
                        i += 3
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
                        while i < len(vettoreEsche):
                            if vettoreEsche[i] == xp and vettoreEsche[i + 1] == yp:
                                confesca = False
                                break
                            i = i + 4
                        for nemico in listaNemici:
                            if nemico.x == xp and nemico.y == yp:
                                confesca = False
                                break
                        if confesca:
                            n = random.randint(1, 2)
                            if abs(xp - x) == abs(yp - y) == 0:
                                npers = 3
                            elif abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
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
                            danno = GlobalVar.dannoOggetti[2]
                            raggio = 0
                            creaesca = True
                            sposta = True
                            risposta = True
                # bomba appiccicosa attacco = 5
                if attacco == 5 and (abs(x - xp) <= GlobalVar.gpx * 5 and abs(y - yp) <= GlobalVar.gpy * 5):
                    # controllo caselle attaccabili
                    continua = True
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                                continua = False
                            break
                        i += 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) == abs(yp - y) == 0:
                            npers = 3
                        elif abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
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
                        danno = GlobalVar.dannoOggetti[3]
                        statom = 2
                        raggio = GlobalVar.gpx * 0
                        sposta = True
                        risposta = True
                # bomba potenziata attacco = 6
                if attacco == 6 and (abs(x - xp) <= GlobalVar.gpx * 4 and abs(y - yp) <= GlobalVar.gpy * 4):
                    # controllo caselle attaccabili
                    continua = True
                    i = 0
                    while i < len(caseattactot):
                        if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                            if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                                continua = False
                            break
                        i += 3
                    if continua:
                        n = random.randint(1, 2)
                        if abs(xp - x) == abs(yp - y) == 0:
                            npers = 3
                        elif abs(xp - x) > abs(yp - y) or (abs(xp - x) == abs(yp - y) and n == 1):
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
                        danno = GlobalVar.dannoOggetti[4]
                        raggio = GlobalVar.gpx * 2
                        sposta = True
                        risposta = True

                nemicoColpito = False
                if infliggidanno and attacco != 1 and (abs(x - xp) <= raggio and abs(y - yp) <= raggio):
                    attaccoDiRallo.append("Rallo")
                    dannoEffettivo = danno - difRallo
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiRallo.append(-dannoEffettivo)
                    pv -= dannoEffettivo
                    if pv <= 0:
                        pv = 0
                        attaccoDiRallo.append("morte")
                    else:
                        if attacco == 3 and not numCollanaIndossata == 1:
                            avvele = True
                            attaccoDiRallo.append("avvelena")
                        elif attacco == 5:
                            attaccoDiRallo.append("appiccica")
                        else:
                            attaccoDiRallo.append("")

                    sposta = True
                    risposta = True
                if infliggidanno and attacco != 1 and (abs(rx - xp) <= raggio and abs(ry - yp) <= raggio):
                    # inquadro il nemico colpito se non sto usando un oggetto
                    if attacco == 1:
                        nemicoInquadrato = "Colco"
                    attaccoDiRallo.append("Colco")
                    dannoEffettivo = danno - difro
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiRallo.append(-dannoEffettivo)
                    enrobVecchia = enrob
                    enrob -= dannoEffettivo
                    if enrob <= 0 and enrobVecchia > 0:
                        enrob = 0
                        attaccoDiRallo.append("morte")
                    else:
                        attaccoDiRallo.append("")

                    sposta = True
                    risposta = True
                for nemico in listaNemici:
                    if infliggidanno and (((abs(nemico.x - xp) <= raggio and abs(nemico.y - yp) <= raggio) and attacco != 1) or ((xp == nemico.x and yp == nemico.y) and attacco == 1)):
                        nemicoColpito = nemico
                        if statom == 1 and nemico.avvelenabile:
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
                i = 0
                while i < len(vettoreEsche):
                    if infliggidanno and vettoreEsche[i + 1] > 0 and (((abs(vettoreEsche[i + 2] - xp) <= raggio and abs(vettoreEsche[i + 3] - yp) <= raggio) and attacco != 1) or ((xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]) and attacco == 1)):
                        nemicoColpito = "Esca:" + str(vettoreEsche[i])
                        vettoreEsche[i + 1] -= danno
                        if vettoreEsche[i + 1] < 0:
                            vettoreEsche[i + 1] = 0
                        # inquadro l'esca colpita se non sto usando un oggetto
                        if attacco == 1:
                            nemicoInquadrato = "Esca" + str(vettoreEsche[i])

                        attaccoDiRallo.append(nemicoColpito)
                        attaccoDiRallo.append(-danno)
                        if vettoreEsche[i + 1] == 0:
                            attaccoDiRallo.append("morte")
                        else:
                            attaccoDiRallo.append("")

                        sposta = True
                        risposta = True
                    i += 4

                # attacco da vicino
                if attacco == 1 and ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)) and sposta and risposta and infliggidanno:
                    attaccato = True
                    if xp == x + GlobalVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalVar.gpy:
                        npers = 3
                # attacco con arco
                elif attacco == 1 and not ((xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)) and sposta and risposta and infliggidanno:
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

                if not risposta and not analisiDiColcoEffettuata:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selimp)

        if ricaricaschermo and not appenaCaricato:
            GlobalVar.schermo.blit(schermoOriginale, (0, 0))
            ricaricaschermo = False
            appenaCaricato = True

        background = schermoOriginale.subsurface(pygame.Rect(xvp, yvp, GlobalVar.gpx, GlobalVar.gpy))
        GlobalVar.schermo.blit(background, (xvp, yvp))
        # visualizza campo attaccabile se sto usando un oggetto
        if attacco == 2:
            campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabile2, (GlobalVar.gpx * 13, GlobalVar.gpy * 13))
            GlobalVar.schermo.blit(campoattaccabile3, (x - (GlobalVar.gpx * 6), y - (GlobalVar.gpy * 6)))
        if attacco == 3:
            campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabile2, (GlobalVar.gpx * 11, GlobalVar.gpy * 11))
            GlobalVar.schermo.blit(campoattaccabile3, (x - (GlobalVar.gpx * 5), y - (GlobalVar.gpy * 5)))
        if attacco == 4:
            campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabile2, (GlobalVar.gpx * 13, GlobalVar.gpy * 13))
            GlobalVar.schermo.blit(campoattaccabile3, (x - (GlobalVar.gpx * 6), y - (GlobalVar.gpy * 6)))
        if attacco == 5:
            campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabile2, (GlobalVar.gpx * 11, GlobalVar.gpy * 11))
            GlobalVar.schermo.blit(campoattaccabile3, (x - (GlobalVar.gpx * 5), y - (GlobalVar.gpy * 5)))
        if attacco == 6:
            campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabile2, (GlobalVar.gpx * 9, GlobalVar.gpy * 9))
            GlobalVar.schermo.blit(campoattaccabile3, (x - (GlobalVar.gpx * 4), y - (GlobalVar.gpy * 4)))

        # movimenti del puntatore su porte e cofanetti quando si usa la tastiera
        if not GlobalVar.mouseVisibile:
            # mettere il puntatore su porte
            i = 0
            while i < len(porte):
                if porte[i + 1] == xp + nxp and porte[i + 2] == yp + nyp and not porte[i + 3]:
                    if nxp != 0 or nyp != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
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
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    puntaCofanetto = True
                    xp = xp + nxp
                    yp = yp + nyp
                    break
                i = i + 4
            # mettere il puntatore sui personaggi-oggetti
            puntaPersonaggioOggetto = False
            for personaggioOggetto in listaPersonaggi:
                if personaggioOggetto.x == xp + nxp and personaggioOggetto.y == yp + nyp:
                    if nxp != 0 or nyp != 0:
                        GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                    puntaPersonaggioOggetto = True
                    xp = xp + nxp
                    yp = yp + nyp
                    break
            if not puntaPorta and not puntaCofanetto and not puntaPersonaggioOggetto:
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == xp + nxp and caseviste[i + 1] == yp + nyp:
                        if caseviste[i + 2]:
                            xp += nxp
                            yp += nyp
                        break
                    i += 3
                if xp != xvp or yp != yvp:
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
            # movimento inquadra quando si è sulle porte
            if puntaPorta:
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == xp + nxp and caseviste[i + 1] == yp + nyp:
                        if caseviste[i + 2]:
                            if nxp != 0 or nyp != 0:
                                GlobalVar.canaleSoundPuntatore.play(GlobalVar.spostaPunBattaglia)
                            xp = xp + nxp
                            yp = yp + nyp
                            puntaPorta = False
                            break
                    i = i + 3

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
                        if (xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy):
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
                i = 0
                while i < len(vettoreEsche):
                    if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                        suPorta = False
                        suCofanetto = False
                        if (xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy):
                            puntatogg = puntatogg2
                        else:
                            puntatogg = puntatogg6
                            j = 0
                            while j < len(caseattactot):
                                if caseattactot[j] == vettoreEsche[i + 2] and caseattactot[j + 1] == vettoreEsche[i + 3]:
                                    if caseattactot[j + 2]:
                                        nemicoInCampoVisivoArco = True
                                    break
                                j += 3
                        break
                    i += 4
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        suPorta = False
                        suCofanetto = False
                        puntatogg = puntatogg7
                        break
            if (((xp == x and yp == y) or (xp == x + GlobalVar.gpx and yp == y) or (xp == x - GlobalVar.gpx and yp == y) or (xp == x and yp == y + GlobalVar.gpy) or (xp == x and yp == y - GlobalVar.gpy)) and puntatogg != 0) or (puntatogg == puntatogg6 and nemicoInCampoVisivoArco and numFrecce > 0):
                puntat = GlobalVar.puntatIn
            else:
                puntat = GlobalVar.puntatOut
        if attacco == 2:
            if abs(x - xp) <= GlobalVar.gpx * 6 and abs(y - yp) <= GlobalVar.gpy * 6:
                puntat = GlobalVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalVar.puntatOut
                        break
                    i = i + 3
            else:
                puntat = GlobalVar.puntatOut
        if attacco == 3:
            if abs(x - xp) <= GlobalVar.gpx * 5 and abs(y - yp) <= GlobalVar.gpy * 5:
                puntat = GlobalVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalVar.puntatOut
                        break
                    i = i + 3
            else:
                puntat = GlobalVar.puntatOut
        if attacco == 4:
            if abs(x - xp) <= GlobalVar.gpx * 6 and abs(y - yp) <= GlobalVar.gpy * 6:
                puntat = GlobalVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalVar.puntatOut
                        break
                    i = i + 3
                i = 0
                while i < len(vettoreDenaro):
                    if vettoreDenaro[i + 1] == xp and vettoreDenaro[i + 2] == yp:
                        puntat = GlobalVar.puntatOut
                        break
                    i += 3
            else:
                puntat = GlobalVar.puntatOut
        if attacco == 5:
            if abs(x - xp) <= GlobalVar.gpx * 5 and abs(y - yp) <= GlobalVar.gpy * 5:
                puntat = GlobalVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalVar.puntatOut
                        break
                    i = i + 3
            else:
                puntat = GlobalVar.puntatOut
        if attacco == 6:
            if abs(x - xp) <= GlobalVar.gpx * 4 and abs(y - yp) <= GlobalVar.gpy * 4:
                puntat = GlobalVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalVar.puntatOut
                        break
                    i = i + 3
            else:
                puntat = GlobalVar.puntatOut
        if puntatogg != 0:
            GlobalVar.schermo.blit(GlobalVar.puntatSfo, (xp, yp))
            GlobalVar.schermo.blit(puntatogg, (xp, yp))
        GlobalVar.schermo.blit(puntat, (xp, yp))

        puntandoSuUnNemicoOColcoOEsca = False
        # disegna vita esche
        i = 0
        while i < len(vettoreEsche):
            if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                puntandoSuUnNemicoOColcoOEsca = True
                lungvita = int(((GlobalVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalVar.schermo.blit(GlobalVar.sfondoEsche, (0, 0))
                GlobalVar.schermo.blit(GlobalVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (int(((GlobalVar.gpx * 1000) / float(4)) // 15), GlobalVar.gpy // 4))
                fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
                vitaesche = pygame.transform.smoothscale(GlobalVar.vitanemico0, (lungvita, GlobalVar.gpy // 4))
                GlobalVar.schermo.blit(indvitamost, (GlobalVar.gpx, 0))
                GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + int(((GlobalVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalVar.schermo.blit(vitaesche, (GlobalVar.gpx, 0))
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
                caseattactotMostri = nemico.caseattactot
                # disegno le caselle non attaccabili
                i = 0
                while i < len(caseattactotMostri):
                    if not caseattactotMostri[i + 2] and not (caseattactotMostri[i] == mx and caseattactotMostri[i + 1] == my):
                        GlobalVar.schermo.blit(GlobalVar.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                    i = i + 3
                campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabilemostro, ((raggiovista * 2) + GlobalVar.gpx, (raggiovista * 2) + GlobalVar.gpy))
                GlobalVar.schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
                GlobalVar.schermo.blit(GlobalVar.sfondoMostro, (0, 0))
                if nemico.avvelenato:
                    GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
                if nemico.appiccicato:
                    GlobalVar.schermo.blit(GlobalVar.appiccicoso, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
                GlobalVar.schermo.blit(nemico.imgS, (0, 0))
                fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
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
                ricaricaschermo = True
                break
        # vita-status-campo visivo robo
        if xp == rx and yp == ry:
            puntandoSuUnNemicoOColcoOEsca = True
            if enrob > 0:
                # controllo caselle attaccabili
                vistaRobo = GlobalVar.gpx * GlobalVar.vistaRobo
                caseattactotRobo = caselleAttaccabiliColco
                # disegno le caselle non attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        GlobalVar.schermo.blit(GlobalVar.caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = GlobalVar.campoattaccabileRobo
                GlobalVar.schermo.blit(campoattaccabile3, (rx - vistaRobo, ry - vistaRobo))
                ricaricaschermo = True
            lungentot = int(((GlobalVar.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVar.gpx * enrob) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.smoothscale(GlobalVar.indvita, (lungentot, GlobalVar.gpy // 4))
            fineindvitarob = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
            vitarob = pygame.transform.smoothscale(GlobalVar.vitarobo, (lungen, GlobalVar.gpy // 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoColco, (0, 0))
            GlobalVar.schermo.blit(indvitarob, (GlobalVar.gpx, 0))
            GlobalVar.schermo.blit(fineindvitarob, (GlobalVar.gpx + lungentot, 0))
            GlobalVar.schermo.blit(vitarob, (GlobalVar.gpx, 0))
            GlobalVar.schermo.blit(GlobalVar.robos, (0, 0))
            if surrisc > 0:
                GlobalVar.schermo.blit(GlobalVar.surriscaldato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if velp > 0:
                GlobalVar.schermo.blit(GlobalVar.velocitapiu, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if effp > 0:
                GlobalVar.schermo.blit(GlobalVar.efficienzapiu, ((GlobalVar.gpx * 3) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        # vita colco selezionato
        if nemicoInquadrato == "Colco" and not puntandoSuUnNemicoOColcoOEsca and avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            if enrob > 0:
                # controllo caselle attaccabili
                vistaRobo = GlobalVar.gpx * GlobalVar.vistaRobo
                caseattactotRobo = caselleAttaccabiliColco
                # disegno le caselle non attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        GlobalVar.schermo.blit(GlobalVar.caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = GlobalVar.campoattaccabileRobo
                GlobalVar.schermo.blit(campoattaccabile3, (rx - vistaRobo, ry - vistaRobo))
            lungentot = int(((GlobalVar.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVar.gpx * enrob) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.smoothscale(GlobalVar.indvita, (lungentot, GlobalVar.gpy // 4))
            fineindvitarob = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
            vitarob = pygame.transform.smoothscale(GlobalVar.vitarobo, (lungen, GlobalVar.gpy // 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoColco, (0, 0))
            GlobalVar.schermo.blit(indvitarob, (GlobalVar.gpx, 0))
            GlobalVar.schermo.blit(fineindvitarob, (GlobalVar.gpx + lungentot, 0))
            GlobalVar.schermo.blit(vitarob, (GlobalVar.gpx, 0))
            GlobalVar.schermo.blit(GlobalVar.robos, (0, 0))
            if surrisc > 0:
                GlobalVar.schermo.blit(GlobalVar.surriscaldato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if velp > 0:
                GlobalVar.schermo.blit(GlobalVar.velocitapiu, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if effp > 0:
                GlobalVar.schermo.blit(GlobalVar.efficienzapiu, ((GlobalVar.gpx * 3) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
        # vita nemico selezionato
        elif not puntandoSuUnNemicoOColcoOEsca and not type(nemicoInquadrato) is str and nemicoInquadrato:
            mx = nemicoInquadrato.x
            my = nemicoInquadrato.y
            pvm = nemicoInquadrato.vita
            pvmtot = nemicoInquadrato.vitaTotale
            raggiovista = nemicoInquadrato.raggioVisivo
            # controllo caselle attaccabili
            caseattactotMostri = nemicoInquadrato.caseattactot
            # disegno le caselle non attaccabili
            i = 0
            while i < len(caseattactotMostri):
                if not caseattactotMostri[i + 2] and not (caseattactotMostri[i] == mx and caseattactotMostri[i + 1] == my):
                    GlobalVar.schermo.blit(GlobalVar.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.smoothscale(GlobalVar.campoattaccabilemostro, ((raggiovista * 2) + GlobalVar.gpx, (raggiovista * 2) + GlobalVar.gpy))
            GlobalVar.schermo.blit(campoattaccabile3, (mx - raggiovista, my - raggiovista))
            GlobalVar.schermo.blit(GlobalVar.sfondoMostro, (0, 0))
            if nemicoInquadrato.avvelenato:
                GlobalVar.schermo.blit(GlobalVar.avvelenato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if nemicoInquadrato.appiccicato:
                GlobalVar.schermo.blit(GlobalVar.appiccicoso, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            GlobalVar.schermo.blit(nemicoInquadrato.imgS, (0, 0))
            fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
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
        # vita esca selezionata
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and not puntandoSuUnNemicoOColcoOEsca:
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vettoreEsche):
                if idEscaInquadrata == vettoreEsche[i]:
                    lungvita = int(((GlobalVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                    if lungvita < 0:
                        lungvita = 0
                    GlobalVar.schermo.blit(GlobalVar.sfondoEsche, (0, 0))
                    GlobalVar.schermo.blit(GlobalVar.esche, (0, 0))
                    indvitamost = pygame.transform.smoothscale(GlobalVar.indvita, (int(((GlobalVar.gpx * 1000) / float(4)) // 15), GlobalVar.gpy // 4))
                    fineindvitamost = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
                    vitaesche = pygame.transform.smoothscale(GlobalVar.vitanemico0, (lungvita, GlobalVar.gpy // 4))
                    GlobalVar.schermo.blit(indvitamost, (GlobalVar.gpx, 0))
                    GlobalVar.schermo.blit(fineindvitamost, (GlobalVar.gpx + int(((GlobalVar.gpx * 1000) / float(4)) // 15), 0))
                    GlobalVar.schermo.blit(vitaesche, (GlobalVar.gpx, 0))
                    break
                i += 4
        # altrimenti mostro solo la vita di colco
        elif not puntandoSuUnNemicoOColcoOEsca and avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            lungentot = int(((GlobalVar.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalVar.gpx * enrob) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.smoothscale(GlobalVar.indvita, (lungentot, GlobalVar.gpy // 4))
            fineindvitarob = pygame.transform.smoothscale(GlobalVar.fineindvita, (GlobalVar.gpx // 12, GlobalVar.gpy // 4))
            vitarob = pygame.transform.smoothscale(GlobalVar.vitarobo, (lungen, GlobalVar.gpy // 4))
            GlobalVar.schermo.blit(GlobalVar.sfondoColco, (0, 0))
            GlobalVar.schermo.blit(indvitarob, (GlobalVar.gpx, 0))
            GlobalVar.schermo.blit(fineindvitarob, (GlobalVar.gpx + lungentot, 0))
            GlobalVar.schermo.blit(vitarob, (GlobalVar.gpx, 0))
            GlobalVar.schermo.blit(GlobalVar.robos, (0, 0))
            if surrisc > 0:
                GlobalVar.schermo.blit(GlobalVar.surriscaldato, (GlobalVar.gpx + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if velp > 0:
                GlobalVar.schermo.blit(GlobalVar.velocitapiu, ((GlobalVar.gpx * 2) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))
            if effp > 0:
                GlobalVar.schermo.blit(GlobalVar.efficienzapiu, ((GlobalVar.gpx * 3) + (GlobalVar.gpx // 8), GlobalVar.gpy // 4))

        # background occhio/chiave
        GlobalVar.schermo.blit(GlobalVar.sfochiaveocchio, (GlobalVar.gsx - (GlobalVar.gpx * 5), 0))
        # vista nemici
        if apriocchio:
            GlobalVar.schermo.blit(GlobalVar.occhioape, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
        else:
            GlobalVar.schermo.blit(GlobalVar.occhiochiu, (GlobalVar.gsx - (GlobalVar.gpx * 1.4), GlobalVar.gpy * 0.3))
        # chiave robo
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
            if chiamarob:
                GlobalVar.schermo.blit(GlobalVar.chiaveroboacc, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))
            else:
                GlobalVar.schermo.blit(GlobalVar.chiaverobospe, (GlobalVar.gsx - (GlobalVar.gpx * 4), 0))

        # disegno img puntatoreInquadraNemici
        if nemicoInquadrato == "Colco":
            if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != rx or vecchiaCasellaInquadrata[2] != ry):
                GlobalVar.schermo.blit(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
            GlobalVar.schermo.blit(GlobalVar.puntatoreInquadraNemici, (rx, ry))
            vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(rx, ry, GlobalVar.gpx, GlobalVar.gpy)), rx, ry]
        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
            if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != nemicoInquadrato.x or vecchiaCasellaInquadrata[2] != nemicoInquadrato.y):
                GlobalVar.schermo.blit(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
            GlobalVar.schermo.blit(GlobalVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
            vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(nemicoInquadrato.x, nemicoInquadrato.y, GlobalVar.gpx, GlobalVar.gpy)), nemicoInquadrato.x, nemicoInquadrato.y]
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vettoreEsche):
                if idEscaInquadrata == vettoreEsche[i]:
                    if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != vettoreEsche[i + 2] or vecchiaCasellaInquadrata[2] != vettoreEsche[i + 3]):
                        GlobalVar.schermo.blit(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
                    GlobalVar.schermo.blit(GlobalVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(vettoreEsche[i + 2], vettoreEsche[i + 3], GlobalVar.gpx, GlobalVar.gpy)), vettoreEsche[i + 2], vettoreEsche[i + 3]]
                    break
                i += 4

        if not risposta:
            pygame.display.update()
        elif not sposta or not attaccato:
            attacco = 0
        pygame.event.pump()
        GlobalVar.clockAttacco.tick(GlobalVar.fpsInquadra)

    return sposta, creaesca, xp, yp, npers, nrob, pv, avvele, enrob, difesa, apriChiudiPorta, apriCofanetto, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac
