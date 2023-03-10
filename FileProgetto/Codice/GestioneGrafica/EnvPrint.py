# -*- coding: utf-8 -*-

import random
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.SettaggiLivelli.SetOstacoliContenutoCofanetti as SetOstacoliContenutoCofanetti
import Codice.GestioneNemiciPersonaggi.MovNemiciRob as MovNemiciRob
import Codice.Localizzazione.LocalizInterfaccia as LI


def disegnaAmbiente(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaro, numFrecce, nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, primaDiAnima, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, avanzamentoStoria, nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcoS, faretraS, armaturaS, collanaS, armaS, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv):
    if caricaTutto:
        GlobalHWVar.disegnaImmagineSuSchermo(imgSfondoStanza, (0, 0))
        # disegno i cadaveri sotterrati
        for nemicoSotterrato in listaNemiciSotterrati:
            GlobalHWVar.disegnaImmagineSuSchermo(imgNemicoSotterrato, (nemicoSotterrato[0], nemicoSotterrato[1]))
        # disegno le bacche
        for baccaPv in listaBacchePv:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgBacchePv, (GlobalHWVar.gpx * baccaPv[0], GlobalHWVar.gpy * baccaPv[1]))
        # salvo la lista di cofanetti vicini a caselle viste per non mettergli la casella oscurata
        vetCofanettiVisti = []
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caselleNonVisibili):
                if ((caselleNonVisibili[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caselleNonVisibili[j + 2]:
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
        # disegna cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caselleNonVisibili):
                if ((caselleNonVisibili[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caselleNonVisibili[j + 2]:
                    if cofanetti[i + 3]:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j += 3
            i += 4
        # disegna porte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                j = 0
                while j < len(casellePercorribiliPorteEscluse):
                    if (casellePercorribiliPorteEscluse[j] == porte[i + 1] - GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] + GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2] - GlobalHWVar.gpy) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2] + GlobalHWVar.gpy):
                        if (casellePercorribiliPorteEscluse[j] == porte[i + 1] - GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] + GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]):
                            if casellePercorribiliPorteEscluse[j + 2]:
                                GlobalHWVar.disegnaImmagineSuSchermo(portaVert, (porte[i + 1], porte[i + 2]))
                            else:
                                GlobalHWVar.disegnaImmagineSuSchermo(portaOriz, (porte[i + 1], porte[i + 2]))
                        else:
                            if casellePercorribiliPorteEscluse[j + 2]:
                                GlobalHWVar.disegnaImmagineSuSchermo(portaOriz, (porte[i + 1], porte[i + 2]))
                            else:
                                GlobalHWVar.disegnaImmagineSuSchermo(portaVert, (porte[i + 1], porte[i + 2]))
                        break
                    j += 3
            i += 4
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
    else:
        # disegnare casella sopra la vecchia posizione e la posizioe attuale di rallo, colco, nemici, personaggi, esche e denaro
        i = 0
        while i < len(vettoreImgCaselle):
            if vx == vettoreImgCaselle[i] and vy == vettoreImgCaselle[i + 1]:
                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            elif vrx == vettoreImgCaselle[i] and vry == vettoreImgCaselle[i + 1]:
                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            elif x == vettoreImgCaselle[i] and y == vettoreImgCaselle[i + 1]:
                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            elif rx == vettoreImgCaselle[i] and ry == vettoreImgCaselle[i + 1]:
                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
            else:
                casellaTrovata = False
                if not casellaTrovata:
                    for nemico in listaNemici:
                        if nemico.x == vettoreImgCaselle[i] and nemico.y == vettoreImgCaselle[i + 1]:
                            if not nemico.morto and nemico.inCasellaVista:
                                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                        if nemico.vx == vettoreImgCaselle[i] and nemico.vy == vettoreImgCaselle[i + 1]:
                            if not nemico.morto and nemico.inCasellaVista:
                                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                                FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                if not casellaTrovata:
                    for personaggio in listaPersonaggi:
                        if personaggio.x == vettoreImgCaselle[i] and personaggio.y == vettoreImgCaselle[i + 1]:
                            if (not personaggio.mantieniSempreASchermo and personaggio.inCasellaVista) or (personaggio.mantieniSempreASchermo and (personaggio.imgAggiornata or caricaTutto)):
                                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                                if not personaggio.mantieniSempreASchermo:
                                    FunzioniGraficheGeneriche.disegnaOmbreggiaturaNellaCasellaSpecifica(vettoreImgCaselle[i], vettoreImgCaselle[i + 1])
                            casellaTrovata = True
                            break
                        if personaggio.vx == vettoreImgCaselle[i] and personaggio.vy == vettoreImgCaselle[i + 1]:
                            if (not personaggio.mantieniSempreASchermo and personaggio.inCasellaVista) or (personaggio.mantieniSempreASchermo and (personaggio.imgAggiornata or caricaTutto)):
                                FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
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
                                        FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
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
                                        FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
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
        sopraCadavere = False
        for personaggio in listaPersonaggi:
            if personaggio.x == vettoreDenaro[i + 1] and personaggio.y == vettoreDenaro[i + 2]:
                sopraCadavere = True
        if not sopraCadavere:
            j = 0
            while j < len(caseviste):
                if caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2]:
                    if caseviste[j + 2]:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                    break
                j += 3
        i += 3

    # robo (anche in caso di raffreddamento e autoricarica)
    if (raffreddamento and not primaDiAnima) or (raffredda >= 0 and not raffreddamento):
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
    elif (ricarica1 and not primaDiAnima) or (autoRic1 >= 0 and not ricarica1):
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    elif (ricarica2 and not primaDiAnima) or (autoRic2 >= 0 and not ricarica2):
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
        if difesa == 0:
            FunzioniGraficheGeneriche.disegnaRallo(avanzamentoStoria, npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
        else:
            FunzioniGraficheGeneriche.disegnaRallo(avanzamentoStoria, npers, x, y, avvele, GlobalImgVar.perss, armaS, armaturaS, scudoDifesa, collanaS, arcoS, faretraS, guantiDifesa, difesa=True)

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
                        FunzioniGraficheGeneriche.disegnaCasellaSulloSchermo(vettoreImgCaselle[i + 2], vettoreImgCaselle[i], vettoreImgCaselle[i + 1], listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv)
                        break
                    i += 3
            if personaggio.imgAttuale:
                GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))
            if not personaggio.vicinoACasellaVista:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaOscurata, (personaggio.x, personaggio.y))
            personaggio.imgAggiornata = False
        elif personaggio.imgAttuale and not personaggio.mantieniSempreASchermo and personaggio.inCasellaVista:
            GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))

    # backbround saltaTurno/occhio/chiave
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 28.5, 0))
    if saltaTurno:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurnoCliccato, (GlobalHWVar.gpx * 30.9, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurno, (GlobalHWVar.gpx * 30.9, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gpx * 29.8, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gpx * 29.8, 0))
    # chiave robo
    if GlobalGameVar.impoPietraPosseduta:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gpx * 28.7, 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gpx * 28.7, 0))

    # vita-status rallo
    FunzioniGraficheGeneriche.disegnaVitaRallo(pv, pvtot, numFrecce, avvele, attp, difp, avanzamentoStoria)

    # disegno la vita del mostro / Colco / esca selezionato
    if nemicoInquadrato == "Colco" or (not nemicoInquadrato and GlobalGameVar.impoPresente):
        FunzioniGraficheGeneriche.disegnaVitaColco(entot, enrob, surrisc, velp, effp)
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
                FunzioniGraficheGeneriche.disegnaVitaEsche(pvEsca)
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
        FunzioniGraficheGeneriche.disegnaVitaNemici(pvm, pvmtot, nemicoAvvelenato, nemicoAppiccicato, nemicoInquadrato.imgS)
    else:
        # mostro l'icona per poter andare in mod. interazione
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoLogoInterazioneNonAttivo, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgModInterazione, (0, 0))

    # disegno img puntatoreInquadraNemici
    if nemicoInquadrato == "Colco":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
    elif not type(nemicoInquadrato) is str and nemicoInquadrato and nemicoInquadrato.vita > 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i] and vettoreEsche[i + 1] > 0:
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


def analizzaColco(schermoBackground, x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, apriocchio, raffredda, autoRic1, autoRic2, mosseRimasteRob, nemicoInquadrato, entot, enrob, surrisc, velp, effp, pv, pvtot, numFrecce, avvele, attp, difp, saltaTurno):
    if raffredda > 0 or autoRic1 > 0 or autoRic2 > 0 or mosseRimasteRob < 0:
        messaggioDiErrore = ""
        if raffredda > 0:
            messaggioDiErrore = LI.RAF_IN_COR[GlobalHWVar.linguaImpostata]
        elif autoRic1 > 0 or autoRic2 > 0:
            messaggioDiErrore = LI.SAC_ENE_IN_CAR[GlobalHWVar.linguaImpostata]
        elif mosseRimasteRob < 0:
            messaggioDiErrore = LI.TEM_TRO_ELE[GlobalHWVar.linguaImpostata]
        vettorePrevisione = [["telecolco", messaggioDiErrore], [1, messaggioDiErrore], [2, messaggioDiErrore], [3, messaggioDiErrore], [4, messaggioDiErrore], [5, messaggioDiErrore], [6, messaggioDiErrore], [7, messaggioDiErrore], [8, messaggioDiErrore], [9, messaggioDiErrore], [10, messaggioDiErrore], ["ultimoObbiettivo", messaggioDiErrore]]
        previsionePosizioneObbiettivi = []
    else:
        vettorePrevisione, previsionePosizioneObbiettivi = MovNemiciRob.movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco=True)

    GlobalHWVar.disegnaImmagineSuSchermo(schermoBackground, (0, 0))

    # disegno img puntatoreInquadraNemici
    if nemicoInquadrato == "Colco":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
        # mostro anche il campo attaccabile
        vistaRobo = GlobalHWVar.gpx * GlobalGameVar.vistaRobo
        i = 0
        while i < len(caselleAttaccabiliColco):
            if not caselleAttaccabiliColco[i + 2] and not (caselleAttaccabiliColco[i] == rx and caselleAttaccabiliColco[i + 1] == ry):
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabiliRobo, (caselleAttaccabiliColco[i], caselleAttaccabiliColco[i + 1]))
            i += 3
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRobo, (rx - vistaRobo, ry - vistaRobo))
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
        FunzioniGraficheGeneriche.disegnaVitaNemici(pvm, pvmtot, nemicoInquadrato.avvelenato, nemicoInquadrato.appiccicato, nemicoInquadrato.imgS)
    # vita esca selezionata
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                FunzioniGraficheGeneriche.disegnaVitaEsche(vettoreEsche[i + 1])
                break
            i += 4
    # altrimenti mostro solo la vita di colco
    elif GlobalGameVar.impoPresente:
        FunzioniGraficheGeneriche.disegnaVitaColco(entot, enrob, surrisc, velp, effp)
    else:
        # mostro l'icona per poter andare in mod. interazione
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoLogoInterazioneNonAttivo, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgModInterazione, (0, 0))

    # vita-status rallo
    FunzioniGraficheGeneriche.disegnaVitaRallo(pv, pvtot, numFrecce, avvele, attp, difp, dati[0])

    # background saltaTurno/occhio/chiave
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 28.5, 0))
    if saltaTurno:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurnoCliccato, (GlobalHWVar.gpx * 30.9, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurno, (GlobalHWVar.gpx * 30.9, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gpx * 29.8, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gpx * 29.8, 0))
    # chiave robo
    if GlobalGameVar.impoPietraPosseduta:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gpx * 28.7, 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gpx * 28.7, 0))

    i = 0
    while i < 32:
        j = 0
        while j < 18:
            casellaObbiettivo = False
            for casella in previsionePosizioneObbiettivi:
                if GlobalHWVar.gpx * i == casella[0] and GlobalHWVar.gpy * j == casella[1]:
                    casellaObbiettivo = True
                    break
            if casellaObbiettivo:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgCasellaObbiettivoAnalizzaColco, (GlobalHWVar.gpx * i, GlobalHWVar.gpy * j))
            j += 1
        i += 1

    if rx < GlobalHWVar.gsx // 32 * 16:
        xPartenzaPannello = GlobalHWVar.gsx // 32 * 19
    else:
        xPartenzaPannello = 0
    dark = pygame.Surface((GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 18), flags=pygame.SRCALPHA)
    dark.fill((0, 0, 0, 160))
    GlobalHWVar.disegnaImmagineSuSchermo(dark, (xPartenzaPannello, 0))

    FunzioniGraficheGeneriche.messaggio(LI.PRE_PRO_AZI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 6.5), GlobalHWVar.gsy // 18 * 1, 65, centrale=True)
    azionePrevistaTrovata = False
    FunzioniGraficheGeneriche.messaggio(LI.MOV_VER_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.8), GlobalHWVar.gsy // 18 * 2.6, 40)
    if vettorePrevisione[0][1] == "":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * 2.5))
        FunzioniGraficheGeneriche.messaggio(LI.IST_ESE_SAL_INT_DI_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 3.2, 35, daDestra=True)
        azionePrevistaTrovata = True
    else:
        FunzioniGraficheGeneriche.messaggio(vettorePrevisione[0][1], GlobalHWVar.rosso, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 3.2, 35, daDestra=True)
    # lista programmazione Colco
    c = 3.7
    for i in range(1, 11):
        if not azionePrevistaTrovata and vettorePrevisione[i][1] == "":
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * c))
            FunzioniGraficheGeneriche.messaggio(LI.IST_ESE_SAL_INT_DI_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * (c + 0.6), 35, daDestra=True)
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
            FunzioniGraficheGeneriche.messaggio(LI.SAR_CON_PV__80[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 2:
            FunzioniGraficheGeneriche.messaggio(LI.SAR_CON_PV__50[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 3:
            FunzioniGraficheGeneriche.messaggio(LI.SAR_CON_PV__30[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 4:
            FunzioniGraficheGeneriche.messaggio(LI.SAR_CON_VEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 5:
            FunzioniGraficheGeneriche.messaggio(LI.IMPO_SURRISCALDATO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 6:
            FunzioniGraficheGeneriche.messaggio(LI.IMP_CON_PE__80[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 7:
            FunzioniGraficheGeneriche.messaggio(LI.IMP_CON_PE__50[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 8:
            FunzioniGraficheGeneriche.messaggio(LI.IMP_CON_PE__30[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 9:
            FunzioniGraficheGeneriche.messaggio(LI.SEM_A_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 10:
            FunzioniGraficheGeneriche.messaggio(LI.SEM_A_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 11:
            FunzioniGraficheGeneriche.messaggio(LI.NEM_A_CAS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 12:
            FunzioniGraficheGeneriche.messaggio(LI.NEMICO_VICINO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 13:
            FunzioniGraficheGeneriche.messaggio(LI.NEMICO_LONTANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 14:
            FunzioniGraficheGeneriche.messaggio(LI.NEM_CON_PV__80[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 15:
            FunzioniGraficheGeneriche.messaggio(LI.NEM_CON_PV__50[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 16:
            FunzioniGraficheGeneriche.messaggio(LI.NEM_CON_PV__30[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 17:
            FunzioniGraficheGeneriche.messaggio(LI.NEM_CON_MEN_PV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 18:
            FunzioniGraficheGeneriche.messaggio(LI.NUM_DI_NEM__1[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 19:
            FunzioniGraficheGeneriche.messaggio(LI.NUM_DI_NEM__2[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 20:
            FunzioniGraficheGeneriche.messaggio(LI.NUM_DI_NEM__3[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaCondizioni, GlobalHWVar.gsy // 18 * c, 40)
        c += 1.1
    xListaTecniche = xPartenzaPannello + (GlobalHWVar.gsx // 32 * 7.2)
    c = 3.8
    for i in range(111, 121):
        if dati[i] == -1:
            FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigioscu, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 0:
            FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 1:
            FunzioniGraficheGeneriche.messaggio(LI.SCOSSA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 2:
            FunzioniGraficheGeneriche.messaggio(LI.CURA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 3:
            FunzioniGraficheGeneriche.messaggio(LI.ANTIDOTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 4:
            FunzioniGraficheGeneriche.messaggio(LI.FRECCIA_ELETTRICA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 5:
            FunzioniGraficheGeneriche.messaggio(LI.TEMPESTA_ELETTRICA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 6:
            FunzioniGraficheGeneriche.messaggio(LI.RAFFREDDAMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 7:
            FunzioniGraficheGeneriche.messaggio(LI.AUTORICARICA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 8:
            FunzioniGraficheGeneriche.messaggio(LI.CURA_P[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 9:
            FunzioniGraficheGeneriche.messaggio(LI.SCOSSA_P[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 10:
            FunzioniGraficheGeneriche.messaggio(LI.FRE_ELE_P[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 11:
            FunzioniGraficheGeneriche.messaggio(LI.VELOCIZZA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 12:
            FunzioniGraficheGeneriche.messaggio(LI.CARICA_ATTACCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 13:
            FunzioniGraficheGeneriche.messaggio(LI.CARICA_DIFESA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 14:
            FunzioniGraficheGeneriche.messaggio(LI.EFFICIENZA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 15:
            FunzioniGraficheGeneriche.messaggio(LI.TEM_ELE_P[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 16:
            FunzioniGraficheGeneriche.messaggio(LI.CURA_PP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 17:
            FunzioniGraficheGeneriche.messaggio(LI.AUTORICARICA_P[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 18:
            FunzioniGraficheGeneriche.messaggio(LI.SCOSSA_PP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 19:
            FunzioniGraficheGeneriche.messaggio(LI.FRE_ELE_PP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        if dati[i] == 20:
            FunzioniGraficheGeneriche.messaggio(LI.TEM_ELE_PP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xListaTecniche, GlobalHWVar.gsy // 18 * c, 40)
        c += 1.1
    FunzioniGraficheGeneriche.messaggio(LI.MOV_VER_OBI_SAL_IN_MEM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.8), GlobalHWVar.gsy // 18 * 14.9, 40)
    if not azionePrevistaTrovata and vettorePrevisione[11][1] == "":
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * 14.8))
        FunzioniGraficheGeneriche.messaggio(LI.IST_ESE_SAL_INT_DI_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 15.5, 35, daDestra=True)
        azionePrevistaTrovata = True
    elif not azionePrevistaTrovata and vettorePrevisione[11][1] != "":
        FunzioniGraficheGeneriche.messaggio(vettorePrevisione[11][1], GlobalHWVar.rosso, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 15.5, 35, daDestra=True)
    FunzioniGraficheGeneriche.messaggio(LI.NES_AZI_DA_ESE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 0.8), GlobalHWVar.gsy // 18 * 16, 40)
    if not azionePrevistaTrovata:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatore, (xPartenzaPannello, GlobalHWVar.gsy // 18 * 15.9))
        FunzioniGraficheGeneriche.messaggio(LI.IST_ESE_SAL_INT_DI_SAR[GlobalHWVar.linguaImpostata], GlobalHWVar.verde, xPartenzaPannello + (GlobalHWVar.gsx // 32 * 12.5), GlobalHWVar.gsy // 18 * 16.6, 35, daDestra=True)

    GlobalHWVar.aggiornaSchermo()

    if not GlobalHWVar.mouseBloccato:
        GlobalHWVar.configuraCursore(True)
    risposta = False
    bottoneDown = False
    while not risposta:
        # gestione degli input
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def attacca(dati, x, y, vx, vy, npers, nrob, rx, ry, obbiettivoCasualeColco, pers, pv, pvtot, difRallo, avvele, numCollanaIndossata, attp, difp, enrob, entot, difro, surrisc, velp, effp, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobS, attVicino, attLontano, attacco, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaro, numFrecce, nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, avanzamentoStoria, casellePercorribili, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, mosseRimasteRob, nonMostrarePersonaggio, saltaTurno, caseattactotRallo, posizioneRalloAggiornamentoCaseAttac, caselleNonVisibili, casellePercorribiliPorteEscluse, listaNemiciSotterrati, imgNemicoSotterrato, listaBacchePv):
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
    # resetto l'animazione del valore dei danni
    GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"] = [False, 0, -1]
    GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"] = [False, 0, -1]
    GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"] = [False, 0, -1]
    GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"] = [False, 0, -1]

    usandoRod = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        usandoRod = True

    puntat = GlobalImgVar.puntatOut
    puntatogg = 0
    puntatogg1 = GlobalImgVar.puntatDif
    puntatogg2 = GlobalImgVar.puntatAtt
    puntatogg3 = GlobalImgVar.puntatPor
    puntatogg4 = GlobalImgVar.puntatAnalisi
    puntatogg5 = GlobalImgVar.puntatCof
    puntatogg6 = GlobalImgVar.puntatArc
    puntatogg7 = GlobalImgVar.puntatDialoghi
    puntatogg8 = GlobalImgVar.puntatDifPv

    # modifica puntatore a seconda dell'attacco
    if attacco == 1:
        puntatogg1 = GlobalImgVar.puntatDif
        puntatogg2 = GlobalImgVar.puntatAtt
        puntatogg3 = GlobalImgVar.puntatPor
        puntatogg4 = GlobalImgVar.puntatAnalisi
        puntatogg5 = GlobalImgVar.puntatCof
        puntatogg6 = GlobalImgVar.puntatArc
        puntatogg7 = GlobalImgVar.puntatDialoghi
        puntatogg8 = GlobalImgVar.puntatDifPv
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

    # controllo caselle attaccabili tue e di Colco
    raggioDiLancio = 0
    if attacco == 1 and (posizioneRalloAggiornamentoCaseAttac[0] != x or posizioneRalloAggiornamentoCaseAttac[1] != y):
        caseattactotRallo = GenericFunc.trovacasattaccabili(x, y, -1, caseviste)
        posizioneRalloAggiornamentoCaseAttac = [x, y]
    if attacco == 2:
        caseattactotRallo = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 6, caseviste)
        raggioDiLancio = 6
        posizioneRalloAggiornamentoCaseAttac = [0, 0]
    if attacco == 3:
        caseattactotRallo = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 5, caseviste)
        raggioDiLancio = 5
        posizioneRalloAggiornamentoCaseAttac = [0, 0]
    if attacco == 4:
        caseattactotRallo = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 6, caseviste)
        raggioDiLancio = 6
        posizioneRalloAggiornamentoCaseAttac = [0, 0]
    if attacco == 5:
        caseattactotRallo = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 5, caseviste)
        raggioDiLancio = 5
        posizioneRalloAggiornamentoCaseAttac = [0, 0]
    if attacco == 6:
        caseattactotRallo = GenericFunc.trovacasattaccabili(x, y, GlobalHWVar.gpx * 4, caseviste)
        raggioDiLancio = 4
        posizioneRalloAggiornamentoCaseAttac = [0, 0]
    # aggiungo tutte le caselle al di fuori del raggio visivo
    if attacco != 1:
        j = 0
        while j < len(caseviste):
            casellaPresente = False
            i = 0
            while i < len(caseattactotRallo):
                if caseattactotRallo[i] == caseviste[j] and caseattactotRallo[i + 1] == caseviste[j + 1]:
                    casellaPresente = True
                    break
                i += 3
            if not casellaPresente:
                caseattactotRallo.append(caseviste[j])
                caseattactotRallo.append(caseviste[j + 1])
                caseattactotRallo.append(False)
            j += 3
        # aggiungo le caselle dei bordi
        i = 0
        while i <= 31:
            if not (abs(x - GlobalHWVar.gpx * i) <= GlobalHWVar.gpx * raggioDiLancio and abs(y - 0) <= GlobalHWVar.gpy * raggioDiLancio):
                caseattactotRallo.append(GlobalHWVar.gpx * i)
                caseattactotRallo.append(0)
                caseattactotRallo.append(False)
            if not (abs(x - GlobalHWVar.gpx * i) <= GlobalHWVar.gpx * raggioDiLancio and abs(y - GlobalHWVar.gpy * 17) <= GlobalHWVar.gpy * raggioDiLancio):
                caseattactotRallo.append(GlobalHWVar.gpx * i)
                caseattactotRallo.append(GlobalHWVar.gpy * 17)
                caseattactotRallo.append(False)
            i += 1
        i = 1
        while i <= 16:
            if not (abs(x - 0) <= GlobalHWVar.gpx * raggioDiLancio and abs(y - GlobalHWVar.gpy * i) <= GlobalHWVar.gpy * raggioDiLancio):
                caseattactotRallo.append(0)
                caseattactotRallo.append(GlobalHWVar.gpy * i)
                caseattactotRallo.append(False)
            if not (abs(x - GlobalHWVar.gpx * 31) <= GlobalHWVar.gpx * raggioDiLancio and abs(y - GlobalHWVar.gpy * i) <= GlobalHWVar.gpy * raggioDiLancio):
                caseattactotRallo.append(GlobalHWVar.gpx * 31)
                caseattactotRallo.append(GlobalHWVar.gpy * i)
                caseattactotRallo.append(False)
            i += 1
    if GlobalGameVar.impoPresente and (posizioneColcoAggiornamentoCaseAttac[0] != rx or posizioneColcoAggiornamentoCaseAttac[1] != ry):
        caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
        posizioneColcoAggiornamentoCaseAttac = [rx, ry]

    listaNemiciVisti = []
    for nemico in listaNemici:
        if nemico.inCasellaVista:
            listaNemiciVisti.append(nemico)

    GlobalHWVar.disegnaImmagineSuSchermo(imgSfondoStanza, (0, 0))
    # disegno i cadaveri sotterrati
    for nemicoSotterrato in listaNemiciSotterrati:
        GlobalHWVar.disegnaImmagineSuSchermo(imgNemicoSotterrato, (nemicoSotterrato[0], nemicoSotterrato[1]))
    # disegno le bacche
    for baccaPv in listaBacchePv:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgBacchePv, (GlobalHWVar.gpx * baccaPv[0], GlobalHWVar.gpy * baccaPv[1]))
    # disegno l'ombreggiatura delle caselle
    i = 0
    while i < len(casellePercorribili):
        if ((casellePercorribili[i] / GlobalHWVar.gpx) + (casellePercorribili[i + 1] / GlobalHWVar.gpy)) % 2 == 0:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaChiara, (casellePercorribili[i], casellePercorribili[i + 1]))
        if ((casellePercorribili[i] / GlobalHWVar.gpx) + (casellePercorribili[i + 1] / GlobalHWVar.gpy)) % 2 == 1:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.casellaScura, (casellePercorribili[i], casellePercorribili[i + 1]))
        i += 2
    # disegna porte
    i = 0
    while i < len(porte):
        if not porte[i + 3]:
            j = 0
            while j < len(casellePercorribiliPorteEscluse):
                if (casellePercorribiliPorteEscluse[j] == porte[i + 1] - GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] + GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2] - GlobalHWVar.gpy) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2] + GlobalHWVar.gpy):
                    if (casellePercorribiliPorteEscluse[j] == porte[i + 1] - GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]) or (casellePercorribiliPorteEscluse[j] == porte[i + 1] + GlobalHWVar.gpx and casellePercorribiliPorteEscluse[j + 1] == porte[i + 2]):
                        if casellePercorribiliPorteEscluse[j + 2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(portaVert, (porte[i + 1], porte[i + 2]))
                        else:
                            GlobalHWVar.disegnaImmagineSuSchermo(portaOriz, (porte[i + 1], porte[i + 2]))
                    else:
                        if casellePercorribiliPorteEscluse[j + 2]:
                            GlobalHWVar.disegnaImmagineSuSchermo(portaOriz, (porte[i + 1], porte[i + 2]))
                        else:
                            GlobalHWVar.disegnaImmagineSuSchermo(portaVert, (porte[i + 1], porte[i + 2]))
                    break
                j += 3
        i += 4
    # disegna cofanetti
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caselleNonVisibili):
            if ((caselleNonVisibili[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caselleNonVisibili[j + 2]:
                if cofanetti[i + 3]:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                break
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
        sopraCadavere = False
        for personaggio in listaPersonaggi:
            if personaggio.x == vettoreDenaro[i + 1] and personaggio.y == vettoreDenaro[i + 2]:
                sopraCadavere = True
        if not sopraCadavere:
            j = 0
            while j < len(caseviste):
                if caseviste[j] == vettoreDenaro[i + 1] and caseviste[j + 1] == vettoreDenaro[i + 2]:
                    if caseviste[j + 2]:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sacchettoDenaro, (vettoreDenaro[i + 1], vettoreDenaro[i + 2]))
                    break
                j += 3
        i += 3
    # robo (anche in caso di raffreddamento e autoricarica)
    if raffredda >= 0:
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
    elif autoRic1 >= 0:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.robomo, (rx, ry))
        imgAnimazione = 0
        i = 0
        while i < len(GlobalImgVar.vetAnimazioniTecniche):
            if GlobalImgVar.vetAnimazioniTecniche[i] == "ricarica":
                imgAnimazione = GlobalImgVar.vetAnimazioniTecniche[i + 1][0]
                break
            i += 2
        GlobalHWVar.disegnaImmagineSuSchermo(imgAnimazione, (rx, ry))
    elif autoRic2 >= 0:
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
        FunzioniGraficheGeneriche.disegnaRallo(avanzamentoStoria, npers, x, y, avvele, pers, arma, armatura, scudo, collana, arco, faretra, guanti)
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
        if personaggio.imgAttuale and (personaggio.mantieniSempreASchermo or personaggio.inCasellaVista):
            GlobalHWVar.disegnaImmagineSuSchermo(personaggio.imgAttuale, (personaggio.x, personaggio.y))

    # disegno le caselle non attaccabili (prima cerco gli oggetti che hanno accanto una casellavista per non oscurarli)
    vetCaselleDaNonOscurare = []
    i = 0
    while i < len(caseattactotRallo):
        if caseattactotRallo[i + 2] or (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
            j = 0
            while j < len(porte):
                if not porte[j + 3]:
                    if (caseattactotRallo[i] == porte[j + 1] - GlobalHWVar.gpx and caseattactotRallo[i + 1] == porte[j + 2]) or (caseattactotRallo[i] == porte[j + 1] + GlobalHWVar.gpx and caseattactotRallo[i + 1] == porte[j + 2]) or (caseattactotRallo[i] == porte[j + 1] and caseattactotRallo[i + 1] == porte[j + 2] - GlobalHWVar.gpy) or (caseattactotRallo[i] == porte[j + 1] and caseattactotRallo[i + 1] == porte[j + 2] + GlobalHWVar.gpy):
                        vetCaselleDaNonOscurare.append(porte[j + 1])
                        vetCaselleDaNonOscurare.append(porte[j + 2])
                j += 4
            j = 0
            while j < len(cofanetti):
                if (caseattactotRallo[i] == cofanetti[j + 1] - GlobalHWVar.gpx and caseattactotRallo[i + 1] == cofanetti[j + 2]) or (caseattactotRallo[i] == cofanetti[j + 1] + GlobalHWVar.gpx and caseattactotRallo[i + 1] == cofanetti[j + 2]) or (caseattactotRallo[i] == cofanetti[j + 1] and caseattactotRallo[i + 1] == cofanetti[j + 2] - GlobalHWVar.gpy) or (caseattactotRallo[i] == cofanetti[j + 1] and caseattactotRallo[i + 1] == cofanetti[j + 2] + GlobalHWVar.gpy):
                    vetCaselleDaNonOscurare.append(cofanetti[j + 1])
                    vetCaselleDaNonOscurare.append(cofanetti[j + 2])
                j += 4
            for personaggio in listaPersonaggi:
                if personaggio.mantieniSempreASchermo and ((personaggio.x == x and (personaggio.y == y + GlobalHWVar.gpy or personaggio.y == y - GlobalHWVar.gpy)) or (personaggio.y == y and (personaggio.x == x + GlobalHWVar.gpx or personaggio.x == x - GlobalHWVar.gpx))):
                    vetCaselleDaNonOscurare.append(personaggio.x)
                    vetCaselleDaNonOscurare.append(personaggio.y)
        i += 3
    i = 0
    while i < len(caseattactotRallo):
        if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
            casellaDaOscurare = True
            j = 0
            while j < len(vetCaselleDaNonOscurare):
                if caseattactotRallo[i] == vetCaselleDaNonOscurare[j] and caseattactotRallo[i + 1] == vetCaselleDaNonOscurare[j + 1]:
                    casellaDaOscurare = False
                    break
                j += 2
            if casellaDaOscurare:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabili, (caseattactotRallo[i], caseattactotRallo[i + 1]))
        i += 3

    # disegno evidenziazione ai personaggi-oggetto interagibili
    for personaggio in listaPersonaggi:
        if personaggio.vicinoACasellaVista or personaggio.inCasellaVista:
            if personaggio.idDialogoCorrente in GlobalGameVar.idDialoghiLetti:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaInterzaioneCompiuta, (personaggio.x, personaggio.y))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaInterzaione, (personaggio.x, personaggio.y))
    # disegno evidenziazione ai cofanetti ancora chiusi (non quando sei Rod o quando usi il calcolatore)
    if not (GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]):
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caselleNonVisibili):
                if ((caselleNonVisibili[j] == cofanetti[i + 1] - GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] + GlobalHWVar.gpx and caselleNonVisibili[j + 1] == cofanetti[i + 2]) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] - GlobalHWVar.gpy) or (caselleNonVisibili[j] == cofanetti[i + 1] and caselleNonVisibili[j + 1] == cofanetti[i + 2] + GlobalHWVar.gpy)) and caselleNonVisibili[j + 2]:
                    if not cofanetti[i + 3]:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaInterzaione, (cofanetti[i + 1], cofanetti[i + 2]))
                    break
                j += 3
            i += 4
    # disegno evidenziazione delle uscite della stanza
    vetEntrate = SetOstacoliContenutoCofanetti.getEntrateStanze(dati[1], avanzamentoStoria)
    i = 0
    while i < len(vetEntrate):
        xUscita = vetEntrate[i] + vetEntrate[i + 2]
        yUscita = vetEntrate[i + 1] + vetEntrate[i + 3]
        if vetEntrate[i + 4] != -1:
            if vetEntrate[i + 3] > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaGiu, (xUscita, yUscita))
            elif vetEntrate[i + 3] < 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaSu, (xUscita, yUscita))
            elif vetEntrate[i + 2] > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaDestra, (xUscita, yUscita))
            elif vetEntrate[i + 2] < 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaSinistra, (xUscita, yUscita))
        else:
            if vetEntrate[i + 3] > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaGiuBloccate, (xUscita, yUscita))
            elif vetEntrate[i + 3] < 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaSuBloccate, (xUscita, yUscita))
            elif vetEntrate[i + 2] > 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaDestraBloccate, (xUscita, yUscita))
            elif vetEntrate[i + 2] < 0:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgEvidenziaUsciteStanzaSinistraBloccate, (xUscita, yUscita))
        i += 5

    schermoOriginale = GlobalHWVar.schermo.copy().convert()

    # vita-status rallo
    FunzioniGraficheGeneriche.disegnaVitaRallo(pv, pvtot, numFrecce, avvele, attp, difp, avanzamentoStoria)

    # background saltaTurno/occhio/chiave
    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 28.5, 0))
    if saltaTurno:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurnoCliccato, (GlobalHWVar.gpx * 30.9, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurno, (GlobalHWVar.gpx * 30.9, 0))
    # vista nemici
    if apriocchio:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gpx * 29.8, 0))
    else:
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gpx * 29.8, 0))
    # chiave robo
    if GlobalGameVar.impoPietraPosseduta:
        if chiamarob:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gpx * 28.7, 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gpx * 28.7, 0))

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
        FunzioniGraficheGeneriche.disegnaVitaNemici(pvm, pvmtot, nemicoInquadrato.avvelenato, nemicoInquadrato.appiccicato, nemicoInquadrato.imgS)
    # vita esca selezionata
    elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
        idEscaInquadrata = int(nemicoInquadrato[4:])
        i = 0
        while i < len(vettoreEsche):
            if idEscaInquadrata == vettoreEsche[i]:
                FunzioniGraficheGeneriche.disegnaVitaEsche(vettoreEsche[i + 1])
                break
            i += 4
    # altrimenti mostro solo la vita di colco
    elif GlobalGameVar.impoPresente:
        FunzioniGraficheGeneriche.disegnaVitaColco(entot, enrob, surrisc, velp, effp)
    else:
        # mostro l'icona per poter andare in mod. interazione
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoLogoInterazioneAttivo, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgModInterazione, (0, 0))

    GlobalHWVar.aggiornaSchermo()

    tastotempfps = 8
    danno = 0
    creaesca = False
    ricaricaschermo = False
    appenaCaricato = True
    suPorta = False
    suCofanetto = False
    apriChiudiPorta = [False, 0, 0]
    apriCofanetto = [False, 0, 0]
    analisiDiColcoEffettuata = False
    puntaPorta = False
    attaccato = False
    attaccoADistanza = False
    sposta = False
    saltaTurno = False
    interagisciConPersonaggio = False
    interazioneConfermata = False
    primoFrame = True
    vecchiaCasellaInquadrata = [False, 0, 0]
    aggiornaInterfacciaPerCambioInput = False
    disegnateCaselleAttaccabili = False
    vecchioNemicoInquadrato = nemicoInquadrato

    bottoneDown = 0
    while not risposta:
        if xp != xvp or yp != yvp:
            appenaCaricato = False
            disegnateCaselleAttaccabili = False
        xvp = xp
        yvp = yp

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (GlobalHWVar.mouseVisibile and (deltaXMouse != 0 or deltaYMouse != 0)) or (primoFrame and GlobalHWVar.mouseVisibile) or (analisiDiColcoEffettuata and GlobalHWVar.mouseVisibile) or (aggiornaInterfacciaPerCambioInput and GlobalHWVar.mouseVisibile):
            casellaTrovata = False
            i = 0
            while i < len(caseviste):
                if caseviste[i] <= xMouse < caseviste[i] + GlobalHWVar.gpx and caseviste[i + 1] <= yMouse < caseviste[i + 1] + GlobalHWVar.gpy and caseviste[i + 2]:
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
                    if cofanetti[i + 1] <= xMouse < cofanetti[i + 1] + GlobalHWVar.gpx and cofanetti[i + 2] <= yMouse < cofanetti[i + 2] + GlobalHWVar.gpy:
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
                    if porte[i + 1] <= xMouse < porte[i + 1] + GlobalHWVar.gpx and porte[i + 2] <= yMouse < porte[i + 2] + GlobalHWVar.gpy:
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
                    if personaggioOggetto.mantieniSempreASchermo and personaggioOggetto.x <= xMouse < personaggioOggetto.x + GlobalHWVar.gpx and personaggioOggetto.y <= yMouse < personaggioOggetto.y + GlobalHWVar.gpy:
                        if personaggioOggetto.vicinoACasellaVista and (xp != personaggioOggetto.x or yp != personaggioOggetto.y):
                            if not primoFrame:
                                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                            xp = xMouse - (xMouse % GlobalHWVar.gpx)
                            yp = yMouse - (yMouse % GlobalHWVar.gpy)
                        casellaTrovata = True
                        break
        if GlobalHWVar.mouseVisibile:
            # controlla se il cursore ?? sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / Rallo / Colco / personaggio / porta / cofanetto / nemico / casella nel raggio (in caso di oggetto)
            if GlobalHWVar.gsy // 18 * 17 <= yMouse <= GlobalHWVar.gsy and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 8:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and GlobalGameVar.impoPresente)) and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 < yMouse < GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 < xMouse < GlobalHWVar.gsx // 32 * 3:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 < yMouse < GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 < xMouse < GlobalHWVar.gsx // 32 * 5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif not nemicoInquadrato and not GlobalGameVar.impoPresente and 0 < yMouse < GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 < xMouse < GlobalHWVar.gsx // 32 * 1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif GlobalGameVar.impoPresente and GlobalGameVar.impoPietraPosseduta and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 28.6 < xMouse <= GlobalHWVar.gsx // 32 * 29.8:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            elif 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 30.8 <= xMouse <= GlobalHWVar.gsx:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "saltaTurno"
            elif y < yMouse < y + GlobalHWVar.gpy and x < xMouse < x + GlobalHWVar.gpx:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "Rallo"
            elif ry < yMouse < ry + GlobalHWVar.gpy and rx < xMouse < rx + GlobalHWVar.gpx and not (nemicoInquadrato == "Colco" and attacco == 4):
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
                                while j < len(caseattactotRallo):
                                    if caseattactotRallo[j] == nemico.x and caseattactotRallo[j + 1] == nemico.y:
                                        if caseattactotRallo[j + 2] and ((abs(nemico.x - x) <= GlobalHWVar.gpx and abs(nemico.y - y) <= GlobalHWVar.gpy and not abs(nemico.x - x) == abs(nemico.y - y)) or (numFrecce > 0 and not usandoRod)) and attacco != 4:
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
                                    while j < len(caseattactotRallo):
                                        if caseattactotRallo[j] == vettoreEsche[i + 2] and caseattactotRallo[j + 1] == vettoreEsche[i + 3]:
                                            if caseattactotRallo[j + 2] and ((abs(vettoreEsche[i + 2] - x) <= GlobalHWVar.gpx and abs(vettoreEsche[i + 3] - y) <= GlobalHWVar.gpy and not abs(vettoreEsche[i + 2] - x) == abs(vettoreEsche[i + 3] - y)) or (numFrecce > 0 and not usandoRod)) and attacco != 4:
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
                        while i < len(caseattactotRallo):
                            if caseattactotRallo[i] <= xMouse <= caseattactotRallo[i] + GlobalHWVar.gpx and caseattactotRallo[i + 1] <= yMouse <= caseattactotRallo[i + 1] + GlobalHWVar.gpy and caseattactotRallo[i + 2]:
                                suPersonaggio = False
                                for personaggio in listaPersonaggi:
                                    if xp == personaggio.x and yp == personaggio.y:
                                        suPersonaggio = True
                                        break
                                suNemico = False
                                for nemico in listaNemici:
                                    if xp == nemico.x and yp == nemico.y:
                                        suNemico = True
                                        break
                                suEsca = False
                                i = 0
                                while i < len(vettoreEsche):
                                    if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                                        suEsca = True
                                        break
                                    i += 4
                                suColco = False
                                if xp == rx and yp == ry:
                                    suColco = True
                                if not suPersonaggio and not ((suNemico or suEsca or suColco) and attacco == 4):
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
        aggiornaInterfacciaPerCambioInput = False

        # gestione degli input
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            nxp = 0
            nyp = 0
            tastotempfps = 8
        # esci
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        # esci e apri il menu
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            risposta = True
            startf = True
            bottoneDown = False
        # esci e salta il turno
        if bottoneDown == pygame.K_0 or bottoneDown == pygame.K_KP0 or bottoneDown == "padSelect":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostaPunBattaglia)
            risposta = True
            sposta = True
            saltaTurno = True
            bottoneDown = False
        # attiva / disattiva il gambit
        if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "padTriangolo":
            if GlobalGameVar.impoPresente and GlobalGameVar.impoPietraPosseduta:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                if chiamarob:
                    chiamarob = False
                else:
                    ultimoObbiettivoColco = []
                    ultimoObbiettivoColco.append("Telecomando")
                    ultimoObbiettivoColco.append(x)
                    ultimoObbiettivoColco.append(y)
                    ultimoObbiettivoColco.append("spostamento")
                    chiamarob = True
            else:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False
        # scorrere il puntatore sui nemici / esche / Colco
        if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
            nemicoInquadratoTemp = False
            # seleziono i nemici / esche visti/e + controllo se il puntatore ?? su un nemico / esca / Colco
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
            # seleziono i nemici / esche visti/e + controllo se il puntatore ?? su un nemico / esca / Colco
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["E"] or bottoneDown == "padQuadrato":
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu":
            suPorta = False
            suCofanetto = False
            nyp = -GlobalHWVar.gpy
            nxp = 0
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra":
            suPorta = False
            suCofanetto = False
            nxp = -GlobalHWVar.gpx
            nyp = 0
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu":
            suPorta = False
            suCofanetto = False
            nyp = GlobalHWVar.gpy
            nxp = 0
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra":
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
                if inquadratoQualcosa == "saltaTurno":
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostaPunBattaglia)
                    risposta = True
                    sposta = True
                    saltaTurno = True
                    bottoneDown = False
                elif inquadratoQualcosa == "start":
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
                        ultimoObbiettivoColco.append("spostamento")
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
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu":
                nyp = -GlobalHWVar.gpy
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra":
                nxp = -GlobalHWVar.gpx
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu":
                nyp = GlobalHWVar.gpy
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra":
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
                # if inquadratoQualcosa == "Colco" and not (type(nemicoInquadrato) is str and nemicoInquadrato == "Colco"):
                #     GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
                #     nemicoInquadrato = "Colco"
                #     daInquadrare = True
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
                    listaNemiciCopiata = GenericFunc.copiaListaDiOggettiConImmagini(listaNemici, True)
                    obbiettivoCasualeColcoCopiato = False
                    if obbiettivoCasualeColco:
                        for nemicoCopiato in listaNemiciCopiata:
                            if obbiettivoCasualeColco.x == nemicoCopiato.x and obbiettivoCasualeColco.y == nemicoCopiato.y:
                                obbiettivoCasualeColcoCopiato = nemicoCopiato
                                break
                    analizzaColco(schermoOriginale, x, y, vx, vy, rx, ry, chiamarob, dati[:], porte[:], listaNemiciCopiata, difesa, ultimoObbiettivoColco[:], obbiettivoCasualeColcoCopiato, GenericFunc.copiaListaDiOggettiConImmagini(listaPersonaggi, False, avanzamentoStoria), caseviste[:], caselleAttaccabiliColco[:], posizioneColcoAggiornamentoCaseAttac[:], vettoreEsche[:], apriocchio, raffredda, autoRic1, autoRic2, mosseRimasteRob, nemicoInquadrato, entot, enrob, surrisc, velp, effp, pv, pvtot, numFrecce, avvele, attp, difp, saltaTurno)
                    analisiDiColcoEffettuata = True
                    GlobalHWVar.disegnaImmagineSuSchermo(schermoOriginale, (0, 0))
                    disegnateCaselleAttaccabili = False
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
                elif attacco == 1 and not ((xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy) or (xp == x and yp == y) or (xp == rx and yp == ry)) and numFrecce > 0 and not usandoRod:
                    j = 0
                    while j < len(caseattactotRallo):
                        if caseattactotRallo[j] == xp and caseattactotRallo[j + 1] == yp:
                            if caseattactotRallo[j + 2]:
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
                    while i < len(caseattactotRallo):
                        if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                            if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                    while i < len(caseattactotRallo):
                        if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                            if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                    while i < len(caseattactotRallo):
                        if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                            if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                        if rx == xp and ry == yp:
                            confesca = False
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
                    while i < len(caseattactotRallo):
                        if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                            if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                    while i < len(caseattactotRallo):
                        if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                            if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, difRallo)
                    attaccoDiRallo.append(-dannoEffettivo)
                    pv -= dannoEffettivo
                    if pv <= 0:
                        pv = 0
                        attaccoDiRallo.append("morte")
                    else:
                        if attacco == 3 and not numCollanaIndossata == 2:
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
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, difro)
                    attaccoDiRallo.append(-dannoEffettivo)
                    enrobVecchia = enrob
                    enrob -= dannoEffettivo
                    if enrob <= 0:
                        enrob = 0
                        if enrobVecchia > 0:
                            attaccoDiRallo.append("morte")
                        else:
                            attaccoDiRallo.append("")
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
                        dannoApprossimato = GenericFunc.calcoloDanni(danno, nemico.difesa)
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
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRallo1, (x - (GlobalHWVar.gpx * 6), y - (GlobalHWVar.gpy * 6)))
        if attacco == 3:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRallo2, (x - (GlobalHWVar.gpx * 5), y - (GlobalHWVar.gpy * 5)))
        if attacco == 4:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRallo3, (x - (GlobalHWVar.gpx * 6), y - (GlobalHWVar.gpy * 6)))
        if attacco == 5:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRallo4, (x - (GlobalHWVar.gpx * 5), y - (GlobalHWVar.gpy * 5)))
        if attacco == 6:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRallo5, (x - (GlobalHWVar.gpx * 4), y - (GlobalHWVar.gpy * 4)))

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
            # movimento inquadra quando si ?? sulle porte
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
                if dati[1] in GlobalGameVar.vetStanzePacifiche and dati[5] < pvtot:
                    puntatogg = puntatogg8
                else:
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
                            while j < len(caseattactotRallo):
                                if caseattactotRallo[j] == nemico.x and caseattactotRallo[j + 1] == nemico.y:
                                    if caseattactotRallo[j + 2]:
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
                            while j < len(caseattactotRallo):
                                if caseattactotRallo[j] == vettoreEsche[i + 2] and caseattactotRallo[j + 1] == vettoreEsche[i + 3]:
                                    if caseattactotRallo[j + 2]:
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
            if (((xp == x and yp == y) or (xp == x + GlobalHWVar.gpx and yp == y) or (xp == x - GlobalHWVar.gpx and yp == y) or (xp == x and yp == y + GlobalHWVar.gpy) or (xp == x and yp == y - GlobalHWVar.gpy)) and puntatogg != 0) or (puntatogg == puntatogg6 and nemicoInCampoVisivoArco and numFrecce > 0 and not usandoRod):
                puntat = GlobalImgVar.puntatIn
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 2:
            if abs(x - xp) <= GlobalHWVar.gpx * 6 and abs(y - yp) <= GlobalHWVar.gpy * 6:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactotRallo):
                    if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                        if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                while i < len(caseattactotRallo):
                    if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                        if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                if xp == rx and yp == ry:
                    puntat = GlobalImgVar.puntatOut
                i = 0
                while i < len(caseattactotRallo):
                    if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                        if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
                            puntat = GlobalImgVar.puntatOut
                        break
                    i += 3
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
                for nemico in listaNemici:
                    if xp == nemico.x and yp == nemico.y:
                        puntat = GlobalImgVar.puntatOut
                        break
                i = 0
                while i < len(vettoreEsche):
                    if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                        puntat = GlobalImgVar.puntatOut
                        break
                    i += 4
            else:
                puntat = GlobalImgVar.puntatOut
        if attacco == 5:
            if abs(x - xp) <= GlobalHWVar.gpx * 5 and abs(y - yp) <= GlobalHWVar.gpy * 5:
                puntat = GlobalImgVar.puntatIn
                i = 0
                while i < len(caseattactotRallo):
                    if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                        if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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
                while i < len(caseattactotRallo):
                    if caseattactotRallo[i] == xp and caseattactotRallo[i + 1] == yp:
                        if not caseattactotRallo[i + 2] and not (caseattactotRallo[i] == x and caseattactotRallo[i + 1] == y):
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

        evitaAggiornamentoImgs = False
        puntandoSuUnNemicoOColcoOEsca = False
        # disegna vita esche
        i = 0
        while i < len(vettoreEsche):
            if xp == vettoreEsche[i + 2] and yp == vettoreEsche[i + 3]:
                if not disegnateCaselleAttaccabili:
                    disegnateCaselleAttaccabili = True
                    ricaricaschermo = True
                    evitaAggiornamentoImgs = True
                puntandoSuUnNemicoOColcoOEsca = True
                FunzioniGraficheGeneriche.disegnaVitaEsche(vettoreEsche[i + 1])
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
                if not disegnateCaselleAttaccabili:
                    # disegno le caselle non attaccabili
                    if not nemico.caselleAttaccabiliAggiornate:
                        nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaro, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=True)
                    caseattactotMostri = nemico.caseattactot
                    i = 0
                    while i < len(caseattactotMostri):
                        if not caseattactotMostri[i + 2] and not (caseattactotMostri[i] == mx and caseattactotMostri[i + 1] == my):
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabilimostro, (caseattactotMostri[i], caseattactotMostri[i + 1]))
                        i += 3
                    GlobalHWVar.disegnaImmagineSuSchermo(nemico.imgCampoAttaccabile, (mx - raggiovista, my - raggiovista))
                    disegnateCaselleAttaccabili = True
                    ricaricaschermo = True
                    evitaAggiornamentoImgs = True
                FunzioniGraficheGeneriche.disegnaVitaNemici(pvm, pvmtot, nemico.avvelenato, nemico.appiccicato, nemico.imgS)
                break
        # vita-status-campo visivo robo
        if xp == rx and yp == ry:
            puntandoSuUnNemicoOColcoOEsca = True
            if not disegnateCaselleAttaccabili:
                if enrob > 0:
                    # disegno le caselle non attaccabili
                    vistaRobo = GlobalHWVar.gpx * GlobalGameVar.vistaRobo
                    i = 0
                    while i < len(caselleAttaccabiliColco):
                        if not caselleAttaccabiliColco[i + 2] and not (caselleAttaccabiliColco[i] == rx and caselleAttaccabiliColco[i + 1] == ry):
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.caselleattaccabiliRobo, (caselleAttaccabiliColco[i], caselleAttaccabiliColco[i + 1]))
                        i += 3
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.campoattaccabileRobo, (rx - vistaRobo, ry - vistaRobo))
                disegnateCaselleAttaccabili = True
                ricaricaschermo = True
                evitaAggiornamentoImgs = True
            FunzioniGraficheGeneriche.disegnaVitaColco(entot, enrob, surrisc, velp, effp)
        # vita colco selezionato
        if nemicoInquadrato == "Colco" and not puntandoSuUnNemicoOColcoOEsca and GlobalGameVar.impoPresente:
            FunzioniGraficheGeneriche.disegnaVitaColco(entot, enrob, surrisc, velp, effp)
        # vita nemico selezionato
        elif not puntandoSuUnNemicoOColcoOEsca and not type(nemicoInquadrato) is str and nemicoInquadrato:
            pvm = nemicoInquadrato.vita
            pvmtot = nemicoInquadrato.vitaTotale
            FunzioniGraficheGeneriche.disegnaVitaNemici(pvm, pvmtot, nemicoInquadrato.avvelenato, nemicoInquadrato.appiccicato, nemicoInquadrato.imgS)
        # vita esca selezionata
        elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and not puntandoSuUnNemicoOColcoOEsca:
            idEscaInquadrata = int(nemicoInquadrato[4:])
            i = 0
            while i < len(vettoreEsche):
                if idEscaInquadrata == vettoreEsche[i]:
                    FunzioniGraficheGeneriche.disegnaVitaEsche(vettoreEsche[i + 1])
                    break
                i += 4
        # altrimenti mostro solo la vita di colco
        elif not puntandoSuUnNemicoOColcoOEsca and GlobalGameVar.impoPresente:
            FunzioniGraficheGeneriche.disegnaVitaColco(entot, enrob, surrisc, velp, effp)
        elif not puntandoSuUnNemicoOColcoOEsca:
            # mostro l'icona per poter andare in mod. interazione
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoLogoInterazioneAttivo, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgModInterazione, (0, 0))

        # vita-status rallo
        FunzioniGraficheGeneriche.disegnaVitaRallo(pv, pvtot, numFrecce, avvele, attp, difp, avanzamentoStoria)

        # background saltaTurno/occhio/chiave
        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfochiaveocchio, (GlobalHWVar.gpx * 28.5, 0))
        if saltaTurno:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurnoCliccato, (GlobalHWVar.gpx * 30.9, 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgSaltaTurno, (GlobalHWVar.gpx * 30.9, 0))
        # vista nemici
        if apriocchio:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhioape, (GlobalHWVar.gpx * 29.8, 0))
        else:
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.occhiochiu, (GlobalHWVar.gpx * 29.8, 0))
        # chiave robo
        if GlobalGameVar.impoPietraPosseduta:
            if chiamarob:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaveroboacc, (GlobalHWVar.gpx * 28.7, 0))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.chiaverobospe, (GlobalHWVar.gpx * 28.7, 0))

        # disegno img puntatoreInquadraNemici
        if nemicoInquadrato == "Colco":
            if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != rx or vecchiaCasellaInquadrata[2] != ry):
                GlobalHWVar.disegnaImmagineSuSchermo(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (rx, ry))
            vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(rx, ry, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert(), rx, ry]
            if vecchioNemicoInquadrato != nemicoInquadrato:
                ricaricaschermo = True
                appenaCaricato = False
                disegnateCaselleAttaccabili = False
                vecchioNemicoInquadrato = nemicoInquadrato
                evitaAggiornamentoImgs = True
        elif not type(nemicoInquadrato) is str and nemicoInquadrato:
            if vecchiaCasellaInquadrata[0] and (vecchiaCasellaInquadrata[1] != nemicoInquadrato.x or vecchiaCasellaInquadrata[2] != nemicoInquadrato.y):
                GlobalHWVar.disegnaImmagineSuSchermo(vecchiaCasellaInquadrata[0], (vecchiaCasellaInquadrata[1], vecchiaCasellaInquadrata[2]))
            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreInquadraNemici, (nemicoInquadrato.x, nemicoInquadrato.y))
            vecchiaCasellaInquadrata = [schermoOriginale.subsurface(pygame.Rect(nemicoInquadrato.x, nemicoInquadrato.y, GlobalHWVar.gpx, GlobalHWVar.gpy)).convert(), nemicoInquadrato.x, nemicoInquadrato.y]
            if vecchioNemicoInquadrato != nemicoInquadrato:
                ricaricaschermo = True
                appenaCaricato = False
                disegnateCaselleAttaccabili = False
                vecchioNemicoInquadrato = nemicoInquadrato
                evitaAggiornamentoImgs = True
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
            if vecchioNemicoInquadrato != nemicoInquadrato:
                ricaricaschermo = True
                appenaCaricato = False
                disegnateCaselleAttaccabili = False
                vecchioNemicoInquadrato = nemicoInquadrato
                evitaAggiornamentoImgs = True

        if not risposta:
            if not evitaAggiornamentoImgs:
                GlobalHWVar.aggiornaSchermo()
        elif not sposta or not attaccato:
            attacco = 0
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockInterazioni.tick(GlobalHWVar.fpsInterazioni)

    return sposta, creaesca, xp, yp, npers, nrob, pv, avvele, enrob, difesa, apriChiudiPorta, apriCofanetto, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, saltaTurno, caseattactotRallo, posizioneRalloAggiornamentoCaseAttac
