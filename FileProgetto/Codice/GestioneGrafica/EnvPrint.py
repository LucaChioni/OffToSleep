# -*- coding: utf-8 -*-

import random
import copy
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import FunzioniGraficheGeneriche
import Codice.GestioneNemiciPersonaggi.MovNemiciRob as MovNemiciRob


def disegnaAmbiente(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, numFrecce, nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, primaDiAnima, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, avanzamentoStoria, nonMostrarePersonaggio):
    if caricaTutto:
        GlobalHWVar.disegnaImmagineSuSchermo(imgSfondoStanza, (0, 0))
        # salvo la lista di cofanetti vicini a ceselle viste per non mettergli la casella oscurata
        vetCofanettiVisti = []
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caseviste[j + 2]:
                    vetCofanettiVisti.append(cofanetti[i + 1])
                    vetCofanettiVisti.append(cofanetti[i + 2])
                j += 3
            i += 4
        # disegno l'ombreggiatura delle caselle percorribili
        i = 0
        while i < len(casellePercorribili):
            if ((casellePercorribili[i] / GlobalHWVar.gpx) + (casellePercorribili[i + 1] / GlobalHWVar.gpy)) % 2 == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
            if ((casellePercorribili[i] / GlobalHWVar.gpx) + (casellePercorribili[i + 1] / GlobalHWVar.gpy)) % 2 == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
            i += 2
        # disegno l'ombreggiatura delle caselle non viste
        caselleNonVisibiliSenzaPorteChiuse = []
        i = 0
        while i < len(caselleNonVisibili):
            if caselleNonVisibili[i + 2]:
                casellaPortaChiusa = False
                j = 0
                while j < len(porte):
                    if not porte[j + 3] and caselleNonVisibili[i] == porte[j + 1] and caselleNonVisibili[i + 1] == porte[j + 2]:
                        casellaPortaChiusa = True
                        break
                    j += 4
                if not casellaPortaChiusa:
                    caselleNonVisibiliSenzaPorteChiuse.append(caselleNonVisibili[i])
                    caselleNonVisibiliSenzaPorteChiuse.append(caselleNonVisibili[i + 1])
            i += 3
        i = 0
        while i < len(caselleNonVisibili):
            if not caselleNonVisibili[i + 2]:
                casellaVicinaACasellaVista = False
                j = 0
                while j < len(caselleNonVisibiliSenzaPorteChiuse):
                    if caselleNonVisibiliSenzaPorteChiuse[j] - GlobalHWVar.gpx <= caselleNonVisibili[i] <= caselleNonVisibiliSenzaPorteChiuse[j] + GlobalHWVar.gpx and caselleNonVisibiliSenzaPorteChiuse[j + 1] - GlobalHWVar.gpy <= caselleNonVisibili[i + 1] <= caselleNonVisibiliSenzaPorteChiuse[j + 1] + GlobalHWVar.gpy:
                        casellaVicinaACasellaVista = True
                        break
                    j += 2
                j = 0
                while j < len(vetCofanettiVisti):
                    if vetCofanettiVisti[j] - GlobalHWVar.gpx <= caselleNonVisibili[i] <= vetCofanettiVisti[j] + GlobalHWVar.gpx and vetCofanettiVisti[j + 1] - GlobalHWVar.gpy <= caselleNonVisibili[i + 1] <= vetCofanettiVisti[j + 1] + GlobalHWVar.gpy:
                        casellaVicinaACasellaVista = True
                        break
                    j += 2
                j = 0
                while j < len(entrateStanza):
                    if entrateStanza[j] + entrateStanza[j + 2] - GlobalHWVar.gpx <= caselleNonVisibili[i] <= entrateStanza[j] + entrateStanza[j + 2] + GlobalHWVar.gpx and entrateStanza[j + 1] + entrateStanza[j + 3] - GlobalHWVar.gpy <= caselleNonVisibili[i + 1] <= entrateStanza[j + 1] + entrateStanza[j + 3] + GlobalHWVar.gpy:
                        k = 0
                        while k < len(caselleNonVisibiliSenzaPorteChiuse):
                            if entrateStanza[j] + entrateStanza[j + 2] - GlobalHWVar.gpx <= caselleNonVisibiliSenzaPorteChiuse[k] <= entrateStanza[j] + entrateStanza[j + 2] + GlobalHWVar.gpx and entrateStanza[j + 1] + entrateStanza[j + 3] - GlobalHWVar.gpy <= caselleNonVisibiliSenzaPorteChiuse[k + 1] <= entrateStanza[j + 1] + entrateStanza[j + 3] + GlobalHWVar.gpy:
                                casellaVicinaACasellaVista = True
                                break
                            k += 2
                        break
                    j += 5
                if not casellaVicinaACasellaVista:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaOscurata, (caselleNonVisibili[i], caselleNonVisibili[i + 1]))
            i += 3

        # disegna porte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                j = 0
                while j < len(caseviste):
                    if ((caseviste[j] == porte[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] and caseviste[j + 1] == porte[i + 2] - GlobalHWVar.gpy) or (caseviste[j] == porte[i + 1] and caseviste[j + 1] == porte[i + 2] + GlobalHWVar.gpy)) and caseviste[j + 2]:
                        if (caseviste[j] == porte[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]):
                            GlobalHWVar.disegnaImmagineSuSchermo(portaVert, (porte[i + 1], porte[i + 2]))
                        else:
                            GlobalHWVar.disegnaImmagineSuSchermo(portaOriz, (porte[i + 1], porte[i + 2]))
                        break
                    j += 3
            i += 4
        # disegna cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caseviste[j + 2]:
                    if cofanetti[i + 3]:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j += 3
            i += 4
    else:
        # disegnare casella sopra la vecchia posizione e la posizioe attuale di rallo, colco, nemici, personaggi, esche e denaro
        i = 0
        while i < len(vettoreImgCaselle):
            if vx == vettoreImgCaselle[i] and vy == vettoreImgCaselle[i + 1]:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            elif vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            elif x == vettoreImgCaselle[i] and y == vettoreImgCaselle[i + 1]:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            elif rx == vettoreImgCaselle[i] and ry == vettoreImgCaselle[i + 1]:
                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            else:
                casellaTrovata = False
                if not casellaTrovata:
                    for nemico in listaNemici:
                        if nemico.x == vettoreImgCaselle[i] and nemico.y == vettoreImgCaselle[i + 1]:
                            if not nemico.morto and nemico.inCasellaVista:
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                        if nemico.vx == vettoreImgCaselle[i] and nemico.vy == vettoreImgCaselle[i + 1]:
                            if not nemico.morto and nemico.inCasellaVista:
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                if not casellaTrovata:
                    for personaggio in listaPersonaggi:
                        if personaggio.x == vettoreImgCaselle[i] and personaggio.y == vettoreImgCaselle[i + 1]:
                            if (not personaggio.mantieniSempreASchermo and personaggio.inCasellaVista) or (personaggio.mantieniSempreASchermo and (personaggio.imgAggiornata or caricaTutto)):
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                if not personaggio.mantieniSempreASchermo:
                                    FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                        if personaggio.vx == vettoreImgCaselle[i] and personaggio.vy == vettoreImgCaselle[i + 1]:
                            if (not personaggio.mantieniSempreASchermo and personaggio.inCasellaVista) or (personaggio.mantieniSempreASchermo and (personaggio.imgAggiornata or caricaTutto)):
                                GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                if not casellaTrovata:
                    j = 0
                    while j < len(vettoreEsche):
                        if vettoreEsche[j + 2] == vettoreImgCaselle[i] and vettoreEsche[j + 3] == vettoreImgCaselle[i + 1]:
                            k = 0
                            while k < len(caseviste):
                                if caseviste[k] == vettoreEsche[j + 2] and caseviste[k + 1] == vettoreEsche[j + 3]:
                                    if caseviste[k + 2] and (primaDiAnima or vettoreEsche[j + 1] > 0):
                                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                                    break
                                k += 3
                            casellaTrovata = True
                            break
                        j += 4
                if not casellaTrovata:
                    j = 0
                    while j < len(vettoreDenaro):
                        if vettoreDenaro[j + 1] == vettoreImgCaselle[i] and vettoreDenaro[j + 2] == vettoreImgCaselle[i + 1]:
                            k = 0
                            while k < len(caseviste):
                                if caseviste[k] == vettoreDenaro[j + 1] and caseviste[k + 1] == vettoreDenaro[j + 2]:
                                    if caseviste[k + 2]:
                                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                                        FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                                    break
                                k += 3
                            casellaTrovata = True
                            break
                        j += 3

            i += 3

    # esche: id, vita, xesca, yesca
    i = 0
    while i < len(vettoreEsche):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3]:
                if caseviste[j + 2] and (primaDiAnima or vettoreEsche[i + 1] > 0):
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            j += 3
        i += 4

    # denaro: qta, x, y
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2]:
                if caseviste[j + 2]:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3

    # robo (anche in caso di raffreddamento e autoricarica)
    if (raffreddamento and not primaDiAnima) or (raffredda > 0 and not raffreddamento):
        GlobalHWVar.disegnaImmagineSuSchermo(armrobS, (rx, ry))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "raffred":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    elif (ricarica1 and not primaDiAnima) or (autoRic1 > 0 and not ricarica1):
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    elif (ricarica2 and not primaDiAnima) or (autoRic2 > 0 and not ricarica2):
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica+":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(robot, (rx, ry))
        if surrisc > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry))
        GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry))

    if not nonMostrarePersonaggio:
        FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

    # disegnare i nemici
    for nemico in listaNemici:
        if not nemico.morto and nemico.inCasellaVista:
            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAttuale, (nemico.x, nemico.y))
            if nemico.avvelenato:
                GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y))
            if nemico.appiccicato:
                GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y))

    # disegno tutti i personaggi
    for personaggio in listaPersonaggi:
        if personaggio.mantieniSempreASchermo and (personaggio.imgAggiornata or caricaTutto):
            if caricaTutto:
                i = 0
                while i < len(vettoreImgCaselle):
                    if personaggio.x == vettoreImgCaselle[i] and personaggio.y == vettoreImgCaselle[i + 1]:
                        GlobalHWVar.disegnaImmagineSuSchermo(vettoreImgCaselle[i + 2], (vettoreImgCaselle[i], vettoreImgCaselle[i + 1]))
                        break
                    i += 3
            GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))
            if not personaggio.vicinoACasellaVista:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaOscurata, (personaggio.x, personaggio.y))
            personaggio.imgAggiornata = False
        elif not personaggio.mantieniSempreASchermo and personaggio.inCasellaVista:
            GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))

    # backbround occhio/chiave
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 27.6, 0, GlobalHWVar.gsx - (GlobalHWVar.gpx * 27.2), GlobalHWVar.gpy * 1.7))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 27, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
    # chiave robo
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))

    # vita-status rallo
    lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
    fineindvitapers = GlobalImgVar.fineindvita
    vitaral = pygame.transform.smoothscale(GlobalImgVar.vitapersonaggio, (lungvita, GlobalHWVar.gpy // 4))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoRallo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(indvitapers, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(fineindvitapers, ((GlobalHWVar.gsx // 32 * 1) + lungvitatot, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(vitaral, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgNumFrecce, (int(GlobalHWVar.gsx // 32 * 1.2), GlobalHWVar.gsy // 18 * 17))
    FunzioniGraficheGeneriche.messaggio(" x" + str(numFrecce), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 17))
    if attp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
    if difp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))

    # disegno la vita del mostro / Colco / esca selezionato
    if nemicoInquadrato == "Colco" or (not nemicoInquadrato and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]):
        lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
        fineindvitarob = GlobalImgVar.fineindvita
        vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
        if surrisc > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if velp > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if effp > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
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
                lungvita = int(((GlobalHWVar.gpx * pvEsca) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), GlobalHWVar.gpy // 4))
                fineindvitamost = GlobalImgVar.fineindvita
                vitaesche = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (lungvita, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitaesche, (GlobalHWVar.gpx, 0))
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
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
        if nemicoAvvelenato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if nemicoAppiccicato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = GlobalImgVar.fineindvita
        if pvmtot > 1500:
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
            lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            if pvm > 15000:
                pvm = 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 13500:
                pvm -= 13500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico8, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 12000:
                pvm -= 12000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico7, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico8
            elif pvm > 10500:
                pvm -= 10500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico6, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico7
            elif pvm > 9000:
                pvm -= 9000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico5, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico6
            elif pvm > 7500:
                pvm -= 7500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico4, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico5
            elif pvm > 6000:
                pvm -= 6000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico3, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico4
            elif pvm > 4500:
                pvm -= 4500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico2, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico3
            elif pvm > 3000:
                pvm -= 3000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico1, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico2
            elif pvm > 1500:
                pvm -= 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico1
            else:
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico0
        else:
            lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (lungvitatot, GlobalHWVar.gpy // 4))
            vitanemico = GlobalImgVar.vitanemico0
        lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
        if lungvita < 0:
            lungvita = 0
        vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanemsucc, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanem, (GlobalHWVar.gpx, 0))

    # disegno img puntatoreInquadraNemici
    if nemicoInquadrato == "Colco":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            i += 4

    if not caricaTutto:
        if stanzaCambiata or uscitoDaMenu > 0:
            if uscitoDaMenu > 0:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=1)
            else:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        else:
            GlobalHWVar.aggiornaSchermo()


def analizzaColco(schermoBackground, x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, apriocchio, raffredda, autoRic1, autoRic2, mosseRimasteRob, nemicoInquadrato, pvtot, pv, numFrecce, avvele, attp, difp, entot, enrob, surrisc, velp, effp):
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
        vettorePrevisione, previsionePosizioneObbiettivi = MovNemiciRob.movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco=True)

    GlobalHWVar.disegnaImmagineSuSchermo(schermoBackground, (0, 0))

    # vita-status rallo
    lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
    fineindvitapers = GlobalImgVar.fineindvita
    vitaral = pygame.transform.smoothscale(GlobalImgVar.vitapersonaggio, (lungvita, GlobalHWVar.gpy // 4))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoRallo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(indvitapers, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(fineindvitapers, ((GlobalHWVar.gsx // 32 * 1) + lungvitatot, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(vitaral, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgNumFrecce, (int(GlobalHWVar.gsx // 32 * 1.2), GlobalHWVar.gsy // 18 * 17))
    FunzioniGraficheGeneriche.messaggio(" x" + str(numFrecce), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 17))
    if attp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
    if difp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))

    # disegno img puntatoreInquadraNemici
    if nemicoInquadrato == "Colco":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            i += 4

    # vita nemico selezionato
    if not type(nemicoInquadrato) is str and nemicoInquadrato:
        pvm = nemicoInquadrato.vita
        pvmtot = nemicoInquadrato.vitaTotale
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
        if nemicoInquadrato.avvelenato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if nemicoInquadrato.appiccicato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = GlobalImgVar.fineindvita
        if pvmtot > 1500:
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
            lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            if pvm > 15000:
                pvm = 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 13500:
                pvm -= 13500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico8, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 12000:
                pvm -= 12000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico7, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico8
            elif pvm > 10500:
                pvm -= 10500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico6, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico7
            elif pvm > 9000:
                pvm -= 9000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico5, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico6
            elif pvm > 7500:
                pvm -= 7500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico4, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico5
            elif pvm > 6000:
                pvm -= 6000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico3, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico4
            elif pvm > 4500:
                pvm -= 4500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico2, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico3
            elif pvm > 3000:
                pvm -= 3000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico1, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico2
            elif pvm > 1500:
                pvm -= 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico1
            else:
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico0
        else:
            lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (lungvitatot, GlobalHWVar.gpy // 4))
            vitanemico = GlobalImgVar.vitanemico0
        lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
        if lungvita < 0:
            lungvita = 0
        vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanemsucc, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanem, (GlobalHWVar.gpx, 0))
    # vita esca selezionata
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                lungvita = int(((GlobalHWVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), GlobalHWVar.gpy // 4))
                fineindvitamost = GlobalImgVar.fineindvita
                vitaesche = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (lungvita, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitaesche, (GlobalHWVar.gpx, 0))
                break
            i += 4
    # altrimenti mostro solo la vita di colco
    elif dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
        lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
        fineindvitarob = GlobalImgVar.fineindvita
        vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
        if surrisc > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if velp > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if effp > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))

    # background occhio/chiave
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 27.6, 0, GlobalHWVar.gsx - (GlobalHWVar.gpx * 27.2), GlobalHWVar.gpy * 1.7))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 27, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
    # chiave robo
    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))

    schermoBackground = GlobalHWVar.schermo.copy().convert()

    i = 0
    while i < 32:
        j = 0
        while j < 18:
            casellaObbiettivo = False
            for casella in previsionePosizioneObbiettivi:
                if GlobalHWVar.gpx * i == casella[0] and GlobalHWVar.gpy * j == casella[1]:
                    casellaObbiettivo = True
                    break
            if not casellaObbiettivo:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaOscurata, (GlobalHWVar.gpx * i, GlobalHWVar.gpy * j))
            j += 1
        i += 1

    if rx < GlobalHWVar.gsx // 32 * 16:
        xPartenzaPannello = GlobalHWVar.gsx // 32 * 19
    else:
        xPartenzaPannello = 0
    backgroundRiquadro = schermoBackground.subsurface(pygame.Rect(xPartenzaPannello, 0, GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 18)).convert()
    dark = pygame.Surface((GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 18), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 180))
    backgroundRiquadro.blit(dark, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(backgroundRiquadro, (xPartenzaPannello, 0))

    FunzioniGraficheGeneriche.messaggio("Previsione prossima azione", GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 1.5), GlobalHWVar.gsy // 18 * 1, 65)
    azionePrevistaTrovata = False
    FunzioniGraficheGeneriche.messaggio("Movimento verso teleImpo", GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.8), GlobalHWVar.gsy // 18 * 2.6, 40)
    if vettorePrevisione[0][1] == "":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * 2.5))
        FunzioniGraficheGeneriche.messaggio("Istruzione eseguita salvo interferenza di Lucy", GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 3.2, 35, daDestra=True)
        azionePrevistaTrovata = True
    else:
        FunzioniGraficheGeneriche.messaggio(vettorePrevisione[0][1], GlobalHWVar.rosso, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 3.2, 35, daDestra=True)
    # lista programmazione Colco
    c = 3.7
    for i in range(1, 11):
        if not azionePrevistaTrovata and vettorePrevisione[i][1] == "":
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * c))
            FunzioniGraficheGeneriche.messaggio("Istruzione eseguita salvo interferenza di Lucy", GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * (c + 0.6), 35, daDestra=True)
            azionePrevistaTrovata = True
        elif not azionePrevistaTrovata and vettorePrevisione[i][1] != "":
            FunzioniGraficheGeneriche.messaggio(vettorePrevisione[i][1], GlobalHWVar.rosso, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * (c + 0.6), 35, daDestra=True)
        if i == 10:
            FunzioniGraficheGeneriche.messaggio(str(i), GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.7), GlobalHWVar.gsy // 18 * c, 50)
        else:
            FunzioniGraficheGeneriche.messaggio(str(i), GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.9), GlobalHWVar.gsy // 18 * c, 50)
        c += 1.1
    xListaCondizioni = xPartenzaPannello + (GlobalHWVar.gsx // 32 * 1.7)
    c = 3.8
    for i in range(101, 111):
        if dati[i] == -1:
            FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigioscu, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 0:
            FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 1:
            FunzioniGraficheGeneriche.messaggio("Lucy con Pv < 80%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 2:
            FunzioniGraficheGeneriche.messaggio("Lucy con Pv < 50%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 3:
            FunzioniGraficheGeneriche.messaggio("Lucy con Pv < 30%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 4:
            FunzioniGraficheGeneriche.messaggio("Lucy con veleno", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 5:
            FunzioniGraficheGeneriche.messaggio("Impo surriscaldato", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 6:
            FunzioniGraficheGeneriche.messaggio("Impo con Pe < 80%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 7:
            FunzioniGraficheGeneriche.messaggio("Impo con Pe < 50%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 8:
            FunzioniGraficheGeneriche.messaggio("Impo con Pe < 30%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 9:
            FunzioniGraficheGeneriche.messaggio("Sempre a Lucy", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 10:
            FunzioniGraficheGeneriche.messaggio("Sempre a Impo", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 11:
            FunzioniGraficheGeneriche.messaggio("Nemico a caso", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 12:
            FunzioniGraficheGeneriche.messaggio("Nemico vicino", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 13:
            FunzioniGraficheGeneriche.messaggio("Nemico lontano", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 14:
            FunzioniGraficheGeneriche.messaggio("Nemico con Pv < 80%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 15:
            FunzioniGraficheGeneriche.messaggio("Nemico con Pv < 50%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 16:
            FunzioniGraficheGeneriche.messaggio("Nemico con Pv < 30%", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 17:
            FunzioniGraficheGeneriche.messaggio("Nemico con meno Pv", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 18:
            FunzioniGraficheGeneriche.messaggio("Numero di nemici > 1", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 19:
            FunzioniGraficheGeneriche.messaggio("Numero di nemici > 4", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 20:
            FunzioniGraficheGeneriche.messaggio("Numero di nemici > 7", GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        c += 1.1
    xListaTecniche = xPartenzaPannello + (GlobalHWVar.gsx // 32 * 7.2)
    c = 3.8
    for i in range(111, 121):
        if dati[i] == -1:
            FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigioscu, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 0:
            FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 1:
            FunzioniGraficheGeneriche.messaggio("Scossa", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 2:
            FunzioniGraficheGeneriche.messaggio("Cura", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 3:
            FunzioniGraficheGeneriche.messaggio("Antidoto", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 4:
            FunzioniGraficheGeneriche.messaggio("Freccia elettrica", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 5:
            FunzioniGraficheGeneriche.messaggio("Tempesta elettrica", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 6:
            FunzioniGraficheGeneriche.messaggio("Raffreddamento", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 7:
            FunzioniGraficheGeneriche.messaggio("Auto-ricarica", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 8:
            FunzioniGraficheGeneriche.messaggio("Cura +", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 9:
            FunzioniGraficheGeneriche.messaggio("Scossa +", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 10:
            FunzioniGraficheGeneriche.messaggio("Freccia elettrica +", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 11:
            FunzioniGraficheGeneriche.messaggio("Velocizza", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 12:
            FunzioniGraficheGeneriche.messaggio("Carica attacco", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 13:
            FunzioniGraficheGeneriche.messaggio("Carica difesa", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 14:
            FunzioniGraficheGeneriche.messaggio("Efficienza", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 15:
            FunzioniGraficheGeneriche.messaggio("Tempesta elettrica +", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 16:
            FunzioniGraficheGeneriche.messaggio("Cura ++", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 17:
            FunzioniGraficheGeneriche.messaggio("Auto-ricarica +", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 18:
            FunzioniGraficheGeneriche.messaggio("Scossa ++", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 19:
            FunzioniGraficheGeneriche.messaggio("Freccia Elettrica ++", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 20:
            FunzioniGraficheGeneriche.messaggio("Tempesta elettrica ++", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        c += 1.1
    FunzioniGraficheGeneriche.messaggio("Movimento verso obbiettivo salvato in memoria", GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.8), GlobalHWVar.gsy // 18 * 14.9, 40)
    if not azionePrevistaTrovata and vettorePrevisione[11][1] == "":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * 14.8))
        FunzioniGraficheGeneriche.messaggio("Istruzione eseguita salvo interferenza di Lucy", GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 15.5, 35, daDestra=True)
        azionePrevistaTrovata = True
    elif not azionePrevistaTrovata and vettorePrevisione[11][1] != "":
        FunzioniGraficheGeneriche.messaggio(vettorePrevisione[11][1], GlobalHWVar.rosso, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 15.5, 35, daDestra=True)
    FunzioniGraficheGeneriche.messaggio("Nessuna azione da eseguire", GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.8), GlobalHWVar.gsy // 18 * 16, 40)
    if not azionePrevistaTrovata:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * 15.9))
        FunzioniGraficheGeneriche.messaggio("Istruzione eseguita salvo interferenza di Lucy", GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 16.6, 35, daDestra=True)

    GlobalHWVar.aggiornaSchermo()

    if not GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(True)
    risposta = False
    bottoneDown = False
    while not risposta:
        # gestione degli input
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def attacca(dati, x, y, vx, vy, npers, nrob, rx, ry, obbiettivoCasualeColco, pers, pv, pvtot, difRallo, avvele, numCollanaIndossata, attp, difp, enrob, entot, difro, surrisc, velp, effp, stanzaa, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, attVicino, attLontano, attacco, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, numFrecce, nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, avanzamentoStoria, casellePercorribili, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, mosseRimasteRob, nonMostrarePersonaggio):
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

    puntat = GlobalImgVar.puntatOut
    puntatogg = 0
    puntatogg1 = GlobalImgVar.puntatDif
    puntatogg2 = GlobalImgVar.puntatAtt
    puntatogg3 = GlobalImgVar.puntatPor
    puntatogg4 = GlobalImgVar.puntatAnalisi
    puntatogg5 = GlobalImgVar.puntatCof
    puntatogg6 = GlobalImgVar.puntatArc
    puntatogg7 = GlobalImgVar.puntatDialoghi

    # modifica puntatore a seconda dell'attacco
    if attacco == 1:
        puntatogg1 = GlobalImgVar.puntatDif
        puntatogg2 = GlobalImgVar.puntatAtt
        puntatogg3 = GlobalImgVar.puntatPor
        puntatogg4 = GlobalImgVar.puntatAnalisi
        puntatogg5 = GlobalImgVar.puntatCof
        puntatogg6 = GlobalImgVar.puntatArc
        puntatogg7 = GlobalImgVar.puntatDialoghi
    if attacco == 2:
        puntatogg = GlobalImgVar.puntatBom
    if attacco == 3:
        puntatogg = GlobalImgVar.puntatBoV
    if attacco == 4:
        puntatogg = GlobalImgVar.puntatEsc
    if attacco == 5:
        puntatogg = GlobalImgVar.puntatBoA
    if attacco == 6:
        puntatogg = GlobalImgVar.puntatBoP

    GlobalHWVar.disegnaImmagineSuSchermo(stanzaa, (0, 0))
    # salvo la lista di cofanetti vicini a ceselle viste per non mettergli la casella oscurata
    vetCofanettiVisti = []
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caseviste[j + 2]:
                vetCofanettiVisti.append(cofanetti[i + 1])
                vetCofanettiVisti.append(cofanetti[i + 2])
            j += 3
        i += 4
    # disegno l'ombreggiatura delle caselle
    i = 0
    while i < len(casellePercorribili):
        if ((casellePercorribili[i] / GlobalHWVar.gpx) + (casellePercorribili[i + 1] / GlobalHWVar.gpy)) % 2 == 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
        if ((casellePercorribili[i] / GlobalHWVar.gpx) + (casellePercorribili[i + 1] / GlobalHWVar.gpy)) % 2 == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
        i += 2

    # controllo caselle attaccabili tue e di Colco
    raggioDiLancio = 0
    caseattactot = []
    if attacco == 1:
        caseattactot = GenericFunc.trovacasattaccabili(x, y, -1, caseviste)
    if attacco == 2:
        caseattactot = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 6, caseviste)
        raggioDiLancio = 6
    if attacco == 3:
        caseattactot = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 5, caseviste)
        raggioDiLancio = 5
    if attacco == 4:
        caseattactot = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 6, caseviste)
        raggioDiLancio = 6
    if attacco == 5:
        caseattactot = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 5, caseviste)
        raggioDiLancio = 5
    if attacco == 6:
        caseattactot = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 4, caseviste)
        raggioDiLancio = 4
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and (posizioneColcoAggiornamentoCaseAttac[0] != rx or posizioneColcoAggiornamentoCaseAttac[1] != ry):
        caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
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
                if ((caseviste[j] == porte[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] and caseviste[j + 1] == porte[i + 2] - GlobalHWVar.gpy) or (caseviste[j] == porte[i + 1] and caseviste[j + 1] == porte[i + 2] + GlobalHWVar.gpy)) and caseviste[j + 2]:
                    if (caseviste[j] == porte[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]) or (caseviste[j] == porte[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == porte[i + 2]):
                        GlobalHWVar.disegnaImmagineSuSchermo(portaVert, (porte[i + 1], porte[i + 2]))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(portaOriz, (porte[i + 1], porte[i + 2]))
                    break
                j += 3
        i += 4
    # disegna cofanetti
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caseviste[j + 2]:
                if cofanetti[i + 3]:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
            j += 3
        i += 4

    # esche: id, vita, xesca, yesca
    i = 0
    while i < len(vettoreEsche):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3]:
                if caseviste[j + 2]:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            j += 3
        i += 4

    # denaro: qta, x, y
    i = 0
    while i < len(vettoreDenaro):
        j = 0
        while j < len(caseviste):
            if caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2]:
                if caseviste[j + 2]:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                break
            j += 3
        i += 3

    # robo (anche in caso di raffreddamento e autoricarica)
    if raffredda > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(armrobS, (rx, ry))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "raffred":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    elif autoRic1 > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    elif autoRic2 > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica+":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(robot, (rx, ry))
        if surrisc > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboSurrisc, (rx, ry))
        GlobalHWVar.disegnaImmagineSuSchermo(armrob, (rx, ry))

    # personaggio
    if not nonMostrarePersonaggio:
        FunzioniGraficheGeneriche.disegnaRallo(npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)

    # disegnare i mostri
    for nemico in listaNemici:
        if nemico.inCasellaVista:
            GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAttuale, (nemico.x, nemico.y))
            if nemico.avvelenato:
                GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAvvelenamento, (nemico.x, nemico.y))
            if nemico.appiccicato:
                GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgAppiccicato, (nemico.x, nemico.y))

    # disegno tutti i personaggi
    for personaggio in listaPersonaggi:
        if personaggio.mantieniSempreASchermo or personaggio.inCasellaVista:
            GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))

    schermoPrevisioneColco = GlobalHWVar.schermo.copy().convert()

    # disegno le caselle non attaccabili (prima cerco gli oggetti che hanno accanto una casellaAttaccabile per non oscurarli)
    vetCaselleDaNonOscurare = []
    i = 0
    while i < len(caseattactot):
        if caseattactot[i + 2] or (caseattactot[i] == x and caseattactot[i + 1] == y):
            j = 0
            while j < len(porte):
                if not porte[j + 3]:
                    if (caseattactot[i] == porte[j + 1] - GlobalHWVar.gpx and caseattactot[i + 1] == porte[j + 2]) or (caseattactot[i] == porte[j + 1] + GlobalHWVar.gpx and caseattactot[i + 1] == porte[j + 2]) or (caseattactot[i] == porte[j + 1] and caseattactot[i + 1] == porte[j + 2] - GlobalHWVar.gpy) or (caseattactot[i] == porte[j + 1] and caseattactot[i + 1] == porte[j + 2] + GlobalHWVar.gpy):
                        vetCaselleDaNonOscurare.append(porte[j + 1])
                        vetCaselleDaNonOscurare.append(porte[j + 2])
                j += 4
            j = 0
            while j < len(cofanetti):
                if (caseattactot[i] == cofanetti[j + 1] - GlobalHWVar.gpx and caseattactot[i + 1] == cofanetti[j + 2]) or (caseattactot[i] == cofanetti[j + 1] + GlobalHWVar.gpx and caseattactot[i + 1] == cofanetti[j + 2]) or (caseattactot[i] == cofanetti[j + 1] and caseattactot[i + 1] == cofanetti[j + 2] - GlobalHWVar.gpy) or (caseattactot[i] == cofanetti[j + 1] and caseattactot[i + 1] == cofanetti[j + 2] + GlobalHWVar.gpy):
                    vetCaselleDaNonOscurare.append(cofanetti[j + 1])
                    vetCaselleDaNonOscurare.append(cofanetti[j + 2])
                j += 4
            for personaggio in listaPersonaggi:
                if personaggio.mantieniSempreASchermo and personaggio.vicinoACasellaVista:
                    if (caseattactot[i] == personaggio.x - GlobalHWVar.gpx and caseattactot[i + 1] == personaggio.y) or (caseattactot[i] == personaggio.x + GlobalHWVar.gpx and caseattactot[i + 1] == personaggio.y) or (caseattactot[i] == personaggio.x and caseattactot[i + 1] == personaggio.y - GlobalHWVar.gpy) or (caseattactot[i] == personaggio.x and caseattactot[i + 1] == personaggio.y + GlobalHWVar.gpy):
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
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
        i += 3

    # vita-status rallo
    lungvitatot = int(((GlobalHWVar.gpx * pvtot) / float(4)) // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
    fineindvitapers = GlobalImgVar.fineindvita
    vitaral = pygame.transform.smoothscale(GlobalImgVar.vitapersonaggio, (lungvita, GlobalHWVar.gpy // 4))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoRallo, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(indvitapers, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(fineindvitapers, ((GlobalHWVar.gsx // 32 * 1) + lungvitatot, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(vitaral, (GlobalHWVar.gsx // 32 * 1, (GlobalHWVar.gsy // 18 * 17) + (GlobalHWVar.gpy // 4 * 3)))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perss, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.perssb, (GlobalHWVar.gsx // 32 * 0, GlobalHWVar.gsy // 18 * 17))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgNumFrecce, (int(GlobalHWVar.gsx // 32 * 1.2), GlobalHWVar.gsy // 18 * 17))
    FunzioniGraficheGeneriche.messaggio(" x" + str(numFrecce), GlobalHWVar.grigiochi, int(GlobalHWVar.gsx // 32 * 1.8), int(GlobalHWVar.gsy // 18 * 17.3), 40)
    if avvele:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 17))
    if attp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.attaccopiu, (GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 17))
    if difp > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.difesapiu, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 17))

    schermoOriginale = GlobalHWVar.schermo.copy().convert()

    # background occhio/chiave
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 27.6, 0, GlobalHWVar.gsx - (GlobalHWVar.gpx * 27.2), GlobalHWVar.gpy * 1.7))
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 27, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
    # chiave robo
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))

    # disegno img puntatoreInquadraNemici
    if nemicoInquadrato == "Colco":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
    elif not type(nemicoInquadrato) is str and nemicoInquadrato:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                break
            i += 4

    # vita nemico selezionato
    if not type(nemicoInquadrato) is str and nemicoInquadrato:
        pvm = nemicoInquadrato.vita
        pvmtot = nemicoInquadrato.vitaTotale
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
        if nemicoInquadrato.avvelenato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if nemicoInquadrato.appiccicato:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(nemicoInquadrato.imgS, (0, 0))
        fineindvitamost = GlobalImgVar.fineindvita
        if pvmtot > 1500:
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
            lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            if pvm > 15000:
                pvm = 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 13500:
                pvm -= 13500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico8, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico9
            elif pvm > 12000:
                pvm -= 12000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico7, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico8
            elif pvm > 10500:
                pvm -= 10500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico6, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico7
            elif pvm > 9000:
                pvm -= 9000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico5, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico6
            elif pvm > 7500:
                pvm -= 7500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico4, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico5
            elif pvm > 6000:
                pvm -= 6000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico3, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico4
            elif pvm > 4500:
                pvm -= 4500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico2, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico3
            elif pvm > 3000:
                pvm -= 3000
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico1, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico2
            elif pvm > 1500:
                pvm -= 1500
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico1
            else:
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico0
        else:
            lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
            indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
            vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (lungvitatot, GlobalHWVar.gpy // 4))
            vitanemico = GlobalImgVar.vitanemico0
        lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
        if lungvita < 0:
            lungvita = 0
        vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanemsucc, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitanem, (GlobalHWVar.gpx, 0))
    # vita esca selezionata
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                lungvita = int(((GlobalHWVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), GlobalHWVar.gpy // 4))
                fineindvitamost = GlobalImgVar.fineindvita
                vitaesche = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (lungvita, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitaesche, (GlobalHWVar.gpx, 0))
                break
            i += 4
    # altrimenti mostro solo la vita di colco
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
        lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
        lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
        fineindvitarob = GlobalImgVar.fineindvita
        vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
        if surrisc > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if velp > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        if effp > 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))

    GlobalHWVar.aggiornaSchermo()

    tastotempfps = 8
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

    bottoneDown = 0
    while not risposta:
        if xp != xvp or yp != yvp:
            appenaCaricato = False
        xvp = xp
        yvp = yp

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (GlobalHWVar.mouseVisibile and (deltaXMouse != 0 or deltaYMouse != 0)) or (primoFrame and GlobalHWVar.mouseVisibile) or (analisiDiColcoEffettuata and GlobalHWVar.mouseVisibile):
            casellaTrovata = False
            i = 0
            while i < len(caseviste):
                if caseviste[i] < xMouse < caseviste[i] + GlobalHWVar.gpx and caseviste[i + 1] < yMouse < caseviste[i + 1] + GlobalHWVar.gpy and caseviste[i + 2]:
                    if xp != caseviste[i] or yp != caseviste[i + 1]:
                        if not primoFrame:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                        xp = xMouse - (xMouse % GlobalHWVar.gpx)
                        yp = yMouse - (yMouse % GlobalHWVar.gpy)
                    casellaTrovata = True
                    break
                i += 3
            if not casellaTrovata:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i + 1] < xMouse < cofanetti[i + 1] + GlobalHWVar.gpx and cofanetti[i + 2] < yMouse < cofanetti[i + 2] + GlobalHWVar.gpy:
                        if xp != cofanetti[i + 1] or yp != cofanetti[i + 2]:
                            j = 0
                            while j < len(caseviste):
                                if ((cofanetti[i + 1] + GlobalHWVar.gpx == caseviste[j] and cofanetti[i + 2] == caseviste[j + 1]) or (cofanetti[i + 1] - GlobalHWVar.gpx == caseviste[j] and cofanetti[i + 2] == caseviste[j + 1]) or (cofanetti[i + 1] == caseviste[j] and cofanetti[i + 2] + GlobalHWVar.gpy == caseviste[j + 1]) or (cofanetti[i + 1] == caseviste[j] and cofanetti[i + 2] - GlobalHWVar.gpy == caseviste[j + 1])) and caseviste[j + 2]:
                                    if not primoFrame:
                                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                                    xp = xMouse - (xMouse % GlobalHWVar.gpx)
                                    yp = yMouse - (yMouse % GlobalHWVar.gpy)
                                    break
                                j += 3
                        casellaTrovata = True
                        break
                    i += 4
            if not casellaTrovata:
                i = 0
                while i < len(porte):
                    if porte[i + 1] < xMouse < porte[i + 1] + GlobalHWVar.gpx and porte[i + 2] < yMouse < porte[i + 2] + GlobalHWVar.gpy:
                        if xp != porte[i + 1] or yp != porte[i + 2]:
                            j = 0
                            while j < len(caseviste):
                                if ((porte[i + 1] + GlobalHWVar.gpx == caseviste[j] and porte[i + 2] == caseviste[j + 1]) or (porte[i + 1] - GlobalHWVar.gpx == caseviste[j] and porte[i + 2] == caseviste[j + 1]) or (porte[i + 1] == caseviste[j] and porte[i + 2] + GlobalHWVar.gpy == caseviste[j + 1]) or (porte[i + 1] == caseviste[j] and porte[i + 2] - GlobalHWVar.gpy == caseviste[j + 1])) and caseviste[j + 2]:
                                    puntaPorta = True
                                    if not primoFrame:
                                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                                    xp = xMouse - (xMouse % GlobalHWVar.gpx)
                                    yp = yMouse - (yMouse % GlobalHWVar.gpy)
                                    break
                                j += 3
                        casellaTrovata = True
                        break
                    i += 4
            if not casellaTrovata:
                for personaggioOggetto in listaPersonaggi:
                    if personaggioOggetto.mantieniSempreASchermo and personaggioOggetto.x < xMouse < personaggioOggetto.x + GlobalHWVar.gpx and personaggioOggetto.y < yMouse < personaggioOggetto.y + GlobalHWVar.gpy:
                        if personaggioOggetto.vicinoACasellaVista and (xp != personaggioOggetto.x or yp != personaggioOggetto.y):
                            if not primoFrame:
                                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                            xp = xMouse - (xMouse % GlobalHWVar.gpx)
                            yp = yMouse - (yMouse % GlobalHWVar.gpy)
                        casellaTrovata = True
                        break
        if GlobalHWVar.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / Rallo / Colco / personaggio / porta / cofanetto / nemico / casella nel raggio (in caso di oggetto)
            if GlobalHWVar.gsy // 18 * 17 <= yMouse <= GlobalHWVar.gsy and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"])) and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 4:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 < yMouse < GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 < xMouse < GlobalHWVar.gsx // 32 * 1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 < yMouse < GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 < xMouse < GlobalHWVar.gsx // 32 * 3:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1.5 and GlobalHWVar.gsx // 32 * 27.8 < xMouse <= GlobalHWVar.gsx // 32 * 30.2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            elif y < yMouse < y + GlobalHWVar.gpy and x < xMouse < x + GlobalHWVar.gpx:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "Rallo"
            elif ry < yMouse < ry + GlobalHWVar.gpy and rx < xMouse < rx + GlobalHWVar.gpx:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "Colco"
            else:
                if not inquadratoQualcosa:
                    for personaggio in listaPersonaggi:
                        if personaggio.x < xMouse < personaggio.x + GlobalHWVar.gpx and personaggio.y < yMouse < personaggio.y + GlobalHWVar.gpy:
                            if attacco == 1 and ((personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy)):
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "personaggio"
                            break
                if not inquadratoQualcosa:
                    for nemico in listaNemiciVisti:
                        if nemico.x < xMouse < nemico.x + GlobalHWVar.gpx and nemico.y < yMouse < nemico.y + GlobalHWVar.gpy:
                            if nemicoInquadrato and type(nemicoInquadrato) is not str and nemico.x == nemicoInquadrato.x and nemico.y == nemicoInquadrato.y:
                                j = 0
                                while j < len(caseattactot):
                                    if caseattactot[j] == nemico.x and caseattactot[j + 1] == nemico.y:
                                        if caseattactot[j + 2] and ((abs(nemico.x - x) <= GlobalHWVar.gpx and abs(nemico.y - y) <= GlobalHWVar.gpy and not abs(nemico.x - x) == abs(nemico.y - y)) or numFrecce > 0):
                                            if GlobalHWVar.mouseBloccato:
                                                GlobalHWVar.configuraCursore(False)
                                            inquadratoQualcosa = "nemico"
                                        break
                                    j += 3
                            elif nemico.inCasellaVista:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "nemico"
                            break
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(vettoreEsche):
                        if vettoreEsche[i + 2] < xMouse < vettoreEsche[i + 2] + GlobalHWVar.gpx and vettoreEsche[i + 3] < yMouse < vettoreEsche[i + 3] + GlobalHWVar.gpy:
                            if nemicoInquadrato and type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                                idEscaInquadrata = int(nemicoInquadrato[4:])
                                if idEscaInquadrata == vettoreEsche[i]:
                                    j = 0
                                    while j < len(caseattactot):
                                        if caseattactot[j] == vettoreEsche[i + 2] and caseattactot[j + 1] == vettoreEsche[i + 3]:
                                            if caseattactot[j + 2] and ((abs(vettoreEsche[i + 2] - x) <= GlobalHWVar.gpx and abs(vettoreEsche[i + 3] - y) <= GlobalHWVar.gpy and not abs(vettoreEsche[i + 2] - x) == abs(vettoreEsche[i + 3] - y)) or numFrecce > 0):
                                                if GlobalHWVar.mouseBloccato:
                                                    GlobalHWVar.configuraCursore(False)
                                                inquadratoQualcosa = "esca"
                                            break
                                        j += 3
                                else:
                                    if GlobalHWVar.mouseBloccato:
                                        GlobalHWVar.configuraCursore(False)
                                    inquadratoQualcosa = "esca"
                            else:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "esca"
                            break
                        i += 4
                if not inquadratoQualcosa and attacco > 1:
                    if x - GlobalHWVar.gpx * raggioDiLancio <= xMouse <= x + GlobalHWVar.gpx + GlobalHWVar.gpx * raggioDiLancio and y - GlobalHWVar.gpy * raggioDiLancio <= yMouse <= y + GlobalHWVar.gpy + GlobalHWVar.gpy * raggioDiLancio:
                        i = 0
                        while i < len(caseattactot):
                            if caseattactot[i] <= xMouse <= caseattactot[i] + GlobalHWVar.gpx and caseattactot[i + 1] <= yMouse <= caseattactot[i + 1] + GlobalHWVar.gpy and caseattactot[i + 2]:
                                suPersonaggio = False
                                for personaggio in listaPersonaggi:
                                    if xp == personaggio.x and yp == personaggio.y:
                                        suPersonaggio = True
                                        break
                                if not suPersonaggio:
                                    if GlobalHWVar.mouseBloccato:
                                        GlobalHWVar.configuraCursore(False)
                                    inquadratoQualcosa = "casellaNelRaggio"
                                break
                            i += 3
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] < xMouse < porte[i + 1] + GlobalHWVar.gpx and porte[i + 2] < yMouse < porte[i + 2] + GlobalHWVar.gpy:
                            if (porte[i + 1] == x + GlobalHWVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalHWVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalHWVar.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalHWVar.gpy):
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "porta"
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] < xMouse < cofanetti[i + 1] + GlobalHWVar.gpx and cofanetti[i + 2] < yMouse < cofanetti[i + 2] + GlobalHWVar.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalHWVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalHWVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalHWVar.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalHWVar.gpy)) and not cofanetti[i + 3]:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto"
                            break
                        i += 4
        if not inquadratoQualcosa:
            if not GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(True)
        primoFrame = False

        # gestione degli input
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
        if bottoneDownVecchio != bottoneDown:
            nxp = 0
            nyp = 0
            tastotempfps = 8
        # esci
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        # esci e apri il menu
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            risposta = True
            startf = True
            bottoneDown = False
        # attiva / disattiva il gambit
        if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "padTriangolo":
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                if chiamarob:
                    chiamarob = False
                else:
                    ultimoObbiettivoColco = []
                    ultimoObbiettivoColco.append("Telecomando")
                    ultimoObbiettivoColco.append(x)
                    ultimoObbiettivoColco.append(y)
                    chiamarob = True
            else:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False
        # scorrere il puntatore sui nemici / esche / Colco
        if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
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
            trovatoNemicoDaInquadrare, nemicoInquadratoTemp = GenericFunc.scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadratoTemp, listaNemiciVisti, listaEscheViste, True)

            if not nemicoInquadratoTemp:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp == "Colco":
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                xp = rx
                yp = ry
            elif not type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                xp = nemicoInquadratoTemp.x
                yp = nemicoInquadratoTemp.y
            elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                xp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 2]
                yp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 3]
            bottoneDown = False
        if bottoneDown == pygame.K_2 or bottoneDown == pygame.K_KP2 or bottoneDown == "padL1":
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
            trovatoNemicoDaInquadrare, nemicoInquadratoTemp = GenericFunc.scorriObbiettiviInquadrati(avanzamentoStoria, nemicoInquadratoTemp, listaNemiciVisti, listaEscheViste, False)

            if not nemicoInquadratoTemp:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp == "Colco":
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                xp = rx
                yp = ry
            elif not type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                xp = nemicoInquadratoTemp.x
                yp = nemicoInquadratoTemp.y
            elif type(nemicoInquadratoTemp) is str and nemicoInquadratoTemp.startswith("Esca"):
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                xp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 2]
                yp = listaEscheViste[listaEscheViste.index(int(nemicoInquadratoTemp[4:])) + 3]
            bottoneDown = False
        # inquadra bersaglio
        if bottoneDown == pygame.K_e or bottoneDown == "padQuadrato":
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
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        # movimento puntatore
        if bottoneDown == pygame.K_w or bottoneDown == "padSu":
            suPorta = False
            suCofanetto = False
            nyp = -GlobalHWVar.gpy
            nxp = 0
        if bottoneDown == pygame.K_a or bottoneDown == "padSinistra":
            suPorta = False
            suCofanetto = False
            nxp = -GlobalHWVar.gpx
            nyp = 0
        if bottoneDown == pygame.K_s or bottoneDown == "padGiu":
            suPorta = False
            suCofanetto = False
            nyp = GlobalHWVar.gpy
            nxp = 0
        if bottoneDown == pygame.K_d or bottoneDown == "padDestra":
            suPorta = False
            suCofanetto = False
            nxp = GlobalHWVar.gpx
            nyp = 0
        # interagisci
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce":
                interazioneConfermata = True
                bottoneDown = False
            elif bottoneDown == "mouseSinistro":
                if inquadratoQualcosa == "start":
                    risposta = True
                    startf = True
                    bottoneDown = False
                elif inquadratoQualcosa == "battaglia":
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                    bottoneDown = False
                elif inquadratoQualcosa == "telecolco":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        chiamarob = True
                    bottoneDown = False
                elif inquadratoQualcosa == "Rallo":
                    interazioneConfermata = True
                    bottoneDown = False
                elif inquadratoQualcosa == "Colco":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "porta":
                    interazioneConfermata = True
                    bottoneDown = False
                elif inquadratoQualcosa == "cofanetto":
                    interazioneConfermata = True
                    bottoneDown = False
                elif inquadratoQualcosa == "personaggio":
                    interazioneConfermata = True
                    bottoneDown = False
                elif inquadratoQualcosa == "nemico":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "esca":
                    interazioneConfermata = True
                elif inquadratoQualcosa == "casellaNelRaggio":
                    interazioneConfermata = True
                    bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            if tastotempfps != 8:
                nxp = 0
                nyp = 0
            tastotempfps -= 1
        if tastotempfps == 0 and bottoneDown:
            if bottoneDown == pygame.K_w or bottoneDown == "padSu":
                nyp = -GlobalHWVar.gpy
            if bottoneDown == pygame.K_a or bottoneDown == "padSinistra":
                nxp = -GlobalHWVar.gpx
            if bottoneDown == pygame.K_s or bottoneDown == "padGiu":
                nyp = GlobalHWVar.gpy
            if bottoneDown == pygame.K_d or bottoneDown == "padDestra":
                nxp = GlobalHWVar.gpx
            tastotempfps = 2

        analisiDiColcoEffettuata = False
        if interazioneConfermata:
            interazioneConfermata = False
            daInquadrare = False
            if bottoneDown == "mouseSinistro" and (inquadratoQualcosa == "nemico" or inquadratoQualcosa == "esca" or inquadratoQualcosa == "Colco"):
                if inquadratoQualcosa == "nemico" and not (nemicoInquadrato and type(nemicoInquadrato) is not str and xp == nemicoInquadrato.x and yp == nemicoInquadrato.y):
                    for nemico in listaNemici:
                        if xp == nemico.x and yp == nemico.y:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
                            nemicoInquadrato = nemico
                            daInquadrare = True
                            break
                if inquadratoQualcosa == "esca":
                    if not (nemicoInquadrato and type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca")):
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
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
                                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
                                    nemicoInquadrato = "Esca" + str(vettoreEsche[i])
                                    daInquadrare = True
                                break
                            i += 4
                if inquadratoQualcosa == "Colco" and not (type(nemicoInquadrato) is str and nemicoInquadrato == "Colco"):
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
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
                if attacco == 1 and ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and suPersonaggio:
                    interagisciConPersonaggio = True
                    risposta = True
                    if xp == x + GlobalHWVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalHWVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalHWVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalHWVar.gpy:
                        npers = 3
                # analizza Colco attacco = 1
                elif attacco == 1 and (xp == rx and yp == ry) and not (rx == x and ry == y):
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    analizzaColco(copy.copy(schermoPrevisioneColco), x, y, vx, vy, rx, ry, chiamarob, dati[:], porte[:], GenericFunc.copiaListaDiOggettiConImmagini(listaNemici, True), difesa, ultimoObbiettivoColco[:], GenericFunc.copiaNemico(obbiettivoCasualeColco), GenericFunc.copiaListaDiOggettiConImmagini(listaPersonaggi, False, avanzamentoStoria), caseviste[:], caselleAttaccabiliColco[:], posizioneColcoAggiornamentoCaseAttac[:], vettoreEsche[:], apriocchio, raffredda, autoRic1, autoRic2, mosseRimasteRob, nemicoInquadrato, pvtot, pv, numFrecce, avvele, attp, difp, entot, enrob, surrisc, velp, effp)
                    analisiDiColcoEffettuata = True
                    GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
                # apri/chiudi porta attacco = 1
                elif attacco == 1 and ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and (suPorta or inquadratoQualcosa == "porta"):
                    apriChiudiPorta = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalHWVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalHWVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalHWVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalHWVar.gpy:
                        npers = 3
                # apri cofanetto attacco = 1
                elif attacco == 1 and ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and (suCofanetto or inquadratoQualcosa == "cofanetto"):
                    apriCofanetto = [True, xp, yp]
                    sposta = True
                    risposta = True
                    if xp == x + GlobalHWVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalHWVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalHWVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalHWVar.gpy:
                        npers = 3
                # attacco ravvicinato attacco = 1
                elif attacco == 1 and ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)):
                    infliggidanno = True
                    danno = attVicino
                    raggio = GlobalHWVar.gpx * 0
                # attacco lontano attacco = 1
                elif attacco == 1 and not ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy) or (xp == x and yp == y) or (xp == rx and yp == ry)) and numFrecce > 0:
                    j = 0
                    while j < len(caseattactot):
                        if caseattactot[j] == xp and caseattactot[j + 1] == yp:
                            if caseattactot[j + 2]:
                                infliggidanno = True
                                danno = attLontano
                                raggio = GlobalHWVar.gpx * 0
                            break
                        j += 3
                # difesa attacco = 1
                elif attacco == 1 and (xp == x and yp == y):
                    difesa = 2
                    risposta = True
                # bomba attacco = 2
                if attacco == 2 and (abs(x - xp) <= GlobalHWVar.gpx * 6 and abs(y - yp) <= GlobalHWVar.gpy * 6) and not suPersonaggio:
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
                        danno = GlobalGameVar.dannoOggetti[0]
                        raggio = GlobalHWVar.gpx * 1
                        sposta = True
                        risposta = True
                # bomba veleno attacco = 3
                if attacco == 3 and (abs(x - xp) <= GlobalHWVar.gpx * 5 and abs(y - yp) <= GlobalHWVar.gpy * 5) and not suPersonaggio:
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
                        danno = GlobalGameVar.dannoOggetti[1]
                        statom = 1
                        raggio = GlobalHWVar.gpx * 0
                        sposta = True
                        risposta = True
                # esca attacco = 4
                if attacco == 4 and (abs(x - xp) <= GlobalHWVar.gpx * 6 and abs(y - yp) <= GlobalHWVar.gpy * 6) and not suPersonaggio:
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
                        # conferma lancio esche
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
                            danno = GlobalGameVar.dannoOggetti[2]
                            raggio = 0
                            creaesca = True
                            sposta = True
                            risposta = True
                # bomba appiccicosa attacco = 5
                if attacco == 5 and (abs(x - xp) <= GlobalHWVar.gpx * 5 and abs(y - yp) <= GlobalHWVar.gpy * 5) and not suPersonaggio:
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
                        danno = GlobalGameVar.dannoOggetti[3]
                        statom = 2
                        raggio = GlobalHWVar.gpx * 0
                        sposta = True
                        risposta = True
                # bomba potenziata attacco = 6
                if attacco == 6 and (abs(x - xp) <= GlobalHWVar.gpx * 4 and abs(y - yp) <= GlobalHWVar.gpy * 4) and not suPersonaggio:
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
                        danno = GlobalGameVar.dannoOggetti[4]
                        raggio = GlobalHWVar.gpx * 2
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
                if attacco == 1 and ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and sposta and risposta and infliggidanno:
                    attaccato = True
                    if xp == x + GlobalHWVar.gpx and yp == y:
                        npers = 1
                    if xp == x - GlobalHWVar.gpx and yp == y:
                        npers = 2
                    if xp == x and yp == y + GlobalHWVar.gpy:
                        npers = 4
                    if xp == x and yp == y - GlobalHWVar.gpy:
                        npers = 3
                # attacco con arco
                elif attacco == 1 and not ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and sposta and risposta and infliggidanno:
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
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        if ricaricaschermo and not appenaCaricato:
            GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
            ricaricaschermo = False
            appenaCaricato = True

        background = schermoOriginale.subsurface(pygame.Rect(xvp, yvp, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert()
        GlobalHWVar.disegnaImmagineSuSchermo(background, (xvp, yvp))
        # visualizza campo attaccabile se sto usando un oggetto
        if attacco == 2:
            campoattaccabile3 = GlobalImgVar.campoattaccabileRallo1
            GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (x - (GlobalHWVar.gpx * 6), y - (GlobalHWVar.gpy * 6)))
        if attacco == 3:
            campoattaccabile3 = GlobalImgVar.campoattaccabileRallo2
            GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (x - (GlobalHWVar.gpx * 5), y - (GlobalHWVar.gpy * 5)))
        if attacco == 4:
            campoattaccabile3 = GlobalImgVar.campoattaccabileRallo3
            GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (x - (GlobalHWVar.gpx * 6), y - (GlobalHWVar.gpy * 6)))
        if attacco == 5:
            campoattaccabile3 = GlobalImgVar.campoattaccabileRallo4
            GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (x - (GlobalHWVar.gpx * 5), y - (GlobalHWVar.gpy * 5)))
        if attacco == 6:
            campoattaccabile3 = GlobalImgVar.campoattaccabileRallo5
            GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (x - (GlobalHWVar.gpx * 4), y - (GlobalHWVar.gpy * 4)))

        # movimenti del puntatore su porte e cofanetti quando si usa la tastiera
        if not GlobalHWVar.mouseVisibile:
            # mettere il puntatore su porte
            i = 0
            while i < len(porte):
                if porte[i + 1] == xp + nxp and porte[i + 2] == yp + nyp and not porte[i + 3]:
                    if nxp != 0 or nyp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
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
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
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
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
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
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
            # movimento inquadra quando si è sulle porte
            if puntaPorta:
                i = 0
                while i < len(caseviste):
                    if caseviste[i] == xp + nxp and caseviste[i + 1] == yp + nyp:
                        if caseviste[i + 2]:
                            if nxp != 0 or nyp != 0:
                                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
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
                        if (xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy):
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
                        if (xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy):
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
            if (((xp == x and yp == y) or (xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and puntatogg != 0) or (puntatogg == puntatogg6 and nemicoInCampoVisivoArco and numFrecce > 0):
                puntat = GlobalImgVar.puntatIn
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 2:
            if abs(x - xp) <= GlobalHWVar.gpx * 6 and abs(y - yp) <= GlobalHWVar.gpy * 6:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalImgVar.puntatOut
                        break
                    i = i + 3
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        puntat = GlobalImgVar.puntatOut
                        break
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 3:
            if abs(x - xp) <= GlobalHWVar.gpx * 5 and abs(y - yp) <= GlobalHWVar.gpy * 5:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalImgVar.puntatOut
                        break
                    i = i + 3
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        puntat = GlobalImgVar.puntatOut
                        break
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 4:
            if abs(x - xp) <= GlobalHWVar.gpx * 6 and abs(y - yp) <= GlobalHWVar.gpy * 6:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalImgVar.puntatOut
                        break
                    i = i + 3
                i = 0
                while i < len(vettoreDenaro):
                    if vettoreDenaro[i + 1] == xp and vettoreDenaro[i + 2] == yp:
                        puntat = GlobalImgVar.puntatOut
                        break
                    i += 3
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        puntat = GlobalImgVar.puntatOut
                        break
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 5:
            if abs(x - xp) <= GlobalHWVar.gpx * 5 and abs(y - yp) <= GlobalHWVar.gpy * 5:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalImgVar.puntatOut
                        break
                    i = i + 3
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        puntat = GlobalImgVar.puntatOut
                        break
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 6:
            if abs(x - xp) <= GlobalHWVar.gpx * 4 and abs(y - yp) <= GlobalHWVar.gpy * 4:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactot):
                    if caseattactot[i] == xp and caseattactot[i + 1] == yp:
                        if not caseattactot[i + 2] and not (caseattactot[i] == x and caseattactot[i + 1] == y):
                            puntat = GlobalImgVar.puntatOut
                        break
                    i = i + 3
                for personaggio in listaPersonaggi:
                    if xp == personaggio.x and yp == personaggio.y:
                        puntat = GlobalImgVar.puntatOut
                        break
            else:
                puntat = GlobalImgVar.puntatOut
        if puntatogg != 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatSfo, (xp, yp))
            GlobalHWVar.disegnaImmagineSuSchermo(puntatogg, (xp, yp))
        GlobalHWVar.disegnaImmagineSuSchermo(puntat, (xp, yp))

        puntandoSuUnNemicoOColcoOEsca = False
        # disegna vita esche
        i = 0
        while i < len(vettoreEsche):
            if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                puntandoSuUnNemicoOColcoOEsca = True
                lungvita = int(((GlobalHWVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), GlobalHWVar.gpy // 4))
                fineindvitamost = GlobalImgVar.fineindvita
                vitaesche = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (lungvita, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitaesche, (GlobalHWVar.gpx, 0))
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
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                    i += 3
                campoattaccabile3 = nemico.imgCampoAttaccabile
                GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (mx - raggiovista, my - raggiovista))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
                if nemico.avvelenato:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
                if nemico.appiccicato:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgS, (0, 0))
                fineindvitamost = GlobalImgVar.fineindvita
                if pvmtot > 1500:
                    indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
                    GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
                    if pvm > 15000:
                        pvm = 1500
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico9
                    elif pvm > 13500:
                        pvm -= 13500
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico8, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico9
                    elif pvm > 12000:
                        pvm -= 12000
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico7, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico8
                    elif pvm > 10500:
                        pvm -= 10500
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico6, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico7
                    elif pvm > 9000:
                        pvm -= 9000
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico5, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico6
                    elif pvm > 7500:
                        pvm -= 7500
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico4, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico5
                    elif pvm > 6000:
                        pvm -= 6000
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico3, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico4
                    elif pvm > 4500:
                        pvm -= 4500
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico2, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico3
                    elif pvm > 3000:
                        pvm -= 3000
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico1, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico2
                    elif pvm > 1500:
                        pvm -= 1500
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico1
                    else:
                        vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                        vitanemico = GlobalImgVar.vitanemico0
                else:
                    lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
                    indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (lungvitatot, GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico0
                lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
                if lungvita < 0:
                    lungvita = 0
                vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitanemsucc, (GlobalHWVar.gpx, 0))
                GlobalHWVar.disegnaImmagineSuSchermo(vitanem, (GlobalHWVar.gpx, 0))
                ricaricaschermo = True
                break
        # vita-status-campo visivo robo
        if xp == rx and yp == ry:
            puntandoSuUnNemicoOColcoOEsca = True
            if enrob > 0:
                # controllo caselle attaccabili
                vistaRobo = GlobalHWVar.gpx * GlobalGameVar.vistaRobo
                caseattactotRobo = caselleAttaccabiliColco
                # disegno le caselle non attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i += 3
                campoattaccabile3 = GlobalImgVar.campoattaccabileRobo
                GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (rx - vistaRobo, ry - vistaRobo))
                ricaricaschermo = True
            lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
            fineindvitarob = GlobalImgVar.fineindvita
            vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
            if surrisc > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if velp > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if effp > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
        # vita colco selezionato
        if nemicoInquadrato == "Colco" and not puntandoSuUnNemicoOColcoOEsca and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
            if enrob > 0:
                # controllo caselle attaccabili
                vistaRobo = GlobalHWVar.gpx * GlobalGameVar.vistaRobo
                caseattactotRobo = caselleAttaccabiliColco
                # disegno le caselle non attaccabili
                i = 0
                while i < len(caseattactotRobo):
                    if not caseattactotRobo[i + 2] and not (caseattactotRobo[i] == rx and caseattactotRobo[i + 1] == ry):
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabiliRobo, (caseattactotRobo[i], caseattactotRobo[i + 1]))
                    i = i + 3
                campoattaccabile3 = GlobalImgVar.campoattaccabileRobo
                GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (rx - vistaRobo, ry - vistaRobo))
            lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
            fineindvitarob = GlobalImgVar.fineindvita
            vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
            if surrisc > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if velp > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if effp > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
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
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                i = i + 3
            campoattaccabile3 = nemicoInquadrato.imgCampoAttaccabile
            GlobalHWVar.disegnaImmagineSuSchermo(campoattaccabile3, (mx - raggiovista, my - raggiovista))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoMostro, (0, 0))
            if nemicoInquadrato.avvelenato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.avvelenato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if nemicoInquadrato.appiccicato:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.appiccicoso, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(nemicoInquadrato.imgS, (0, 0))
            fineindvitamost = GlobalImgVar.fineindvita
            if pvmtot > 1500:
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                lungvitatot = int(((GlobalHWVar.gpx * 1500) / float(4)) // 15)
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
                if pvm > 15000:
                    pvm = 1500
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico9
                elif pvm > 13500:
                    pvm -= 13500
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico8, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico9
                elif pvm > 12000:
                    pvm -= 12000
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico7, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico8
                elif pvm > 10500:
                    pvm -= 10500
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico6, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico7
                elif pvm > 9000:
                    pvm -= 9000
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico5, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico6
                elif pvm > 7500:
                    pvm -= 7500
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico4, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico5
                elif pvm > 6000:
                    pvm -= 6000
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico3, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico4
                elif pvm > 4500:
                    pvm -= 4500
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico2, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico3
                elif pvm > 3000:
                    pvm -= 3000
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico1, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico2
                elif pvm > 1500:
                    pvm -= 1500
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico1
                else:
                    vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (int(((GlobalHWVar.gpx * 1500) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    vitanemico = GlobalImgVar.vitanemico0
            else:
                lungvitatot = int(((GlobalHWVar.gpx * pvmtot) / float(4)) // 15)
                indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungvitatot, GlobalHWVar.gpy // 4))
                GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + lungvitatot, 0))
                vitanemsucc = pygame.transform.smoothscale(GlobalImgVar.vitanemico00, (lungvitatot, GlobalHWVar.gpy // 4))
                vitanemico = GlobalImgVar.vitanemico0
            lungvita = int(((GlobalHWVar.gpx * pvm) / float(4)) // 15)
            if lungvita < 0:
                lungvita = 0
            vitanem = pygame.transform.smoothscale(vitanemico, (lungvita, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vitanemsucc, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vitanem, (GlobalHWVar.gpx, 0))
        # vita esca selezionata
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and not puntandoSuUnNemicoOColcoOEsca:
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vettoreEsche):
                if idEscaInquadrata == vettoreEsche[i]:
                    lungvita = int(((GlobalHWVar.gpx * vettoreEsche[i + 1]) / float(4)) // 15)
                    if lungvita < 0:
                        lungvita = 0
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoEsche, (0, 0))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.esche, (0, 0))
                    indvitamost = pygame.transform.smoothscale(GlobalImgVar.indvita, (int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), GlobalHWVar.gpy // 4))
                    fineindvitamost = GlobalImgVar.fineindvita
                    vitaesche = pygame.transform.smoothscale(GlobalImgVar.vitanemico0, (lungvita, GlobalHWVar.gpy // 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(indvitamost, (GlobalHWVar.gpx, 0))
                    GlobalHWVar.disegnaImmagineSuSchermo(fineindvitamost, (GlobalHWVar.gpx + int(((GlobalHWVar.gpx * 1000) / float(4)) // 15), 0))
                    GlobalHWVar.disegnaImmagineSuSchermo(vitaesche, (GlobalHWVar.gpx, 0))
                    break
                i += 4
        # altrimenti mostro solo la vita di colco
        elif not puntandoSuUnNemicoOColcoOEsca and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
            lungentot = int(((GlobalHWVar.gpx * entot) / float(4)) // 15)
            lungen = int(((GlobalHWVar.gpx * enrob) / float(4)) // 15)
            if lungen < 0:
                lungen = 0
            indvitarob = pygame.transform.smoothscale(GlobalImgVar.indvita, (lungentot, GlobalHWVar.gpy // 4))
            fineindvitarob = GlobalImgVar.fineindvita
            vitarob = pygame.transform.smoothscale(GlobalImgVar.vitarobo, (lungen, GlobalHWVar.gpy // 4))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoColco, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(indvitarob, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(fineindvitarob, (GlobalHWVar.gpx + lungentot, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vitarob, (GlobalHWVar.gpx, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robos, (0, 0))
            if surrisc > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.surriscaldato, (GlobalHWVar.gpx + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if velp > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.velocitapiu, ((GlobalHWVar.gpx * 2) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))
            if effp > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.efficienzapiu, ((GlobalHWVar.gpx * 3) + (GlobalHWVar.gpx // 8), GlobalHWVar.gpy // 4))

        # background occhio/chiave
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 27.6, 0, GlobalHWVar.gsx - (GlobalHWVar.gpx * 27.2), GlobalHWVar.gpy * 1.7))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 27, 0))
        # vista nemici
        if apriocchio:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 1.4), GlobalHWVar.gpy * 0.3))
        # chiave robo
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
            if chiamarob:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gsx - (GlobalHWVar.gpx * 4), 0))

        # disegno img puntatoreInquadraNemici
        if nemicoInquadrato == "Colco":
            if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != rx or vecchiaCasellaInquadrata[2] != ry):
                GlobalHWVar.disegnaImmagineSuSchermo(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
            vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(rx, ry, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert(), rx, ry]
        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
            if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != nemicoInquadrato.x or vecchiaCasellaInquadrata[2] != nemicoInquadrato.y):
                GlobalHWVar.disegnaImmagineSuSchermo(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
            vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(nemicoInquadrato.x, nemicoInquadrato.y, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert(), nemicoInquadrato.x, nemicoInquadrato.y]
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vettoreEsche):
                if idEscaInquadrata == vettoreEsche[i]:
                    if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != vettoreEsche[i + 2] or vecchiaCasellaInquadrata[2] != vettoreEsche[i + 3]):
                        GlobalHWVar.disegnaImmagineSuSchermo(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (vettoreEsche[i + 2], vettoreEsche[i + 3]))
                    vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(vettoreEsche[i + 2], vettoreEsche[i + 3], GlobalHWVar.gpx, GlobalHWVar.gpy)).convert(), vettoreEsche[i + 2], vettoreEsche[i + 3]]
                    break
                i += 4

        if not risposta:
            GlobalHWVar.aggiornaSchermo()
        elif not sposta or not attaccato:
            attacco = 0
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockInterazioni.tick(GlobalHWVar.fpsInterazioni)

    return sposta, creaesca, xp, yp, npers, nrob, pv, avvele, enrob, difesa, apriChiudiPorta, apriCofanetto, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac
