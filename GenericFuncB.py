# -*- coding: utf-8 -*-

from NemicoObj import *
from PersonaggioObj import *


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata,stanza, stanzaVecchia, canzone, inizio):
    # npers: 1=d, 2=a, 3=w, 4=s
    if stanza == GlobalVar.dictStanze["sognoSara1"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteSogno
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteSogno
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara2"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["sognoSara2"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteSogno
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteSogno
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara1"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 7
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara3"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
                y = GlobalVar.gsy // 18 * 3
    if stanza == GlobalVar.dictStanze["sognoSara3"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteSogno
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteSogno
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara2"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                y = GlobalVar.gsy // 18 * 11
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 14
                y = GlobalVar.gsy // 18 * 2
    if stanza == GlobalVar.dictStanze["sognoSara4"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteSogno
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteSogno
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara3"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamSara1"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporte1
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporte1
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 3
                y = GlobalVar.gsy // 18 * 14
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara2"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamSara2"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporte1
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporte1
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara1"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara3"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 3:
                    x = GlobalVar.gsx // 32 * 3
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 4:
                    x = GlobalVar.gsx // 32 * 4
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 27:
                    x = GlobalVar.gsx // 32 * 27
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 28:
                    x = GlobalVar.gsx // 32 * 28
                    y = GlobalVar.gsy // 18 * 2
    if stanza == GlobalVar.dictStanze["casaSamSara3"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporte1
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporte1
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara2"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 3:
                    x = GlobalVar.gsx // 32 * 3
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 4:
                    x = GlobalVar.gsx // 32 * 4
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 27:
                    x = GlobalVar.gsx // 32 * 27
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 28:
                    x = GlobalVar.gsx // 32 * 28
                    y = GlobalVar.gsy // 18 * 15

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, canzone


def caricaNemiciEPersonaggi(avanzamentoStoria, stanza, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali):
    listaNemici = []
    if not stanza in stanzeGiaVisitate:
        if stanza == GlobalVar.dictStanze["sognoSara2"]:
            percorsoNemico = ["s", "d", "d", "w", "w", "w", "a", "a", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 7, "s", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "s", "w", "w"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 2, "s", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "d", "d", "a", "a", "a", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4, "d", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["sognoSara3"]:
            percorsoNemico = ["a", "a", "a", "w", "w", "w", "d", "d", "d", "s", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8, "s", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "s", "s", "s", "a", "a", "s", "a", "w", "w", "w", "w", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 5, "d", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "s", "a", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 10, "w", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "s", "a", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 10, "w", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    else:
        for nemico in listaNemiciTotali:
            if nemico.stanzaDiAppartenenza == stanza:
                listaNemici.append(nemico)
    nmost = len(listaNemici)

    listaPersonaggi = []
    if not stanza in stanzeGiaVisitate:
        if stanza == GlobalVar.dictStanze["casaSamSara1"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 13, "a", "OggettoLettoSara", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, "d", "OggettoLavandinoCucina", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, "s", "OggettoLavandinoBagno", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, "a", "OggettoScaffaleBicchieriA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 6, "a", "OggettoScaffaleBicchieriB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 7, "a", "OggettoScaffaleBicchieriC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 14, "w", "OggettoComodinoSara", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 15, "w", "OggettoFinestraA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 15, "w", "OggettoFinestraB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 12, "d", "OggettoLettoSam", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 3, "s", "OggettoDocciaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 3, "s", "OggettoDocciaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 2, "s", "OggettoDocciaC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, "d", "OggettoGabinettoA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 3, "d", "OggettoGabinettoB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, "d", "OggettoGabinettoC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 4, "s", "OggettoCaminoA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4, "s", "OggettoCaminoB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 4, "s", "OggettoCaminoC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 5, "s", "OggettoCaminoD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6, "s", "OggettoCaminoE", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 6, "s", "OggettoCaminoF", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 6, "s", "OggettoCaminoG", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["casaSamSara2"]:
            percorsoPersonaggio = ["d", "d", "s", "s", "d", "s", "s", "s", "a", "a", "w", "w", "a", "s", "a", "a", "a", "w", "w", "w", "d", "d", "w", "d"]
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 6, "d", "CaneCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 10, "d", "CaneCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    else:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == stanza:
                listaPersonaggi.append(personaggio)

    if not stanza in stanzeGiaVisitate:
        stanzeGiaVisitate.append(stanza)

    return nmost, listaNemici, listaPersonaggi, listaNemiciTotali, listaPersonaggiTotali


def gestisciEventiStoria(avanzamentoStoria, stanza, x, y, cambiosta, carim, caricaTutto, tastop, movimentoPerMouse, impossibileAprirePorta, canzone):
    if impossibileAprirePorta:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True

    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["inizio"] and stanza == GlobalVar.dictStanze["sognoSara1"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara1"] and stanza == GlobalVar.dictStanze["sognoSara1"]:
        personaggio = PersonaggioObj(False, False, False, "Tutorial", False, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"] and stanza == GlobalVar.dictStanze["sognoSara1"]:
        personaggio = PersonaggioObj(False, False, False, "Tutorial", False, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanza == GlobalVar.dictStanze["sognoSara2"]:
        personaggio = PersonaggioObj(False, False, False, "Tutorial", False, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialBattaglia"] and stanza == GlobalVar.dictStanze["sognoSara3"]:
        personaggio = PersonaggioObj(False, False, False, "Tutorial", False, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"] and stanza == GlobalVar.dictStanze["sognoSara3"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara2"] and stanza == GlobalVar.dictStanze["sognoSara4"] and x == GlobalVar.gpx * 15 and y == GlobalVar.gpy * 8:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        stanza = GlobalVar.dictStanze["casaSamSara1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaSamSara1"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj(False, False, False, "OggettoLettoSara", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] and stanza == GlobalVar.dictStanze["casaSamSara1"] and x == GlobalVar.gpx * 6 and y == GlobalVar.gpy * 8:
        personaggio = PersonaggioObj(False, False, False, "Tutorial", False, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        caricaTutto = True

    if caricaTutto:
        movimentoPerMouse = False
        tastop = 0
    return avanzamentoStoria, cambiosta, stanza, carim, caricaTutto, tastop, movimentoPerMouse


def nonPuoiProcedere(avanzamentoStoria, x, y, stanzaVecchia, stanzaDestinazione, canzone):
    nonProcedere = False
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalVar.dictStanze["sognoSara1"] and stanzaDestinazione == GlobalVar.dictStanze["sognoSara2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        nonProcedere = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] and stanzaVecchia == GlobalVar.dictStanze["casaSamSara1"] and stanzaDestinazione == GlobalVar.dictStanze["casaSamSara2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        nonProcedere = True
    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaSamSara1"] and xPorta == GlobalVar.gpx * 25 and yPorta == GlobalVar.gpy * 3:
        procedi = False
    return procedi
