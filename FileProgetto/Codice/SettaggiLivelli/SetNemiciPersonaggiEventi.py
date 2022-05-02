# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizSogno as PosizSogno
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCasa as PosizCasaHansSara
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizForestaCadetta as PosizForestaCadetta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizStradaPerCitta as PosizStradaPerCitta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCitta as PosizCitta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCasaUfficiale as PosizCasaUfficiale
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizBiblioteca as PosizBiblioteca
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizStradaPerSelvaArida as PosizStradaPerSelvaArida
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizSelvaArida as PosizSelvaArida
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizAvampostoDiRod as PosizAvampostoDiRod
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizLabirinto as PosizLabirinto
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizEsternoCastello as PosizEsternoCastello
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizInternoCastello as PosizInternoCastello
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizScorciatoiaLabirinto as PosizScorciatoiaLabirinto
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizStradaPerPassoMontano as PosizStradaPerPassoMontano
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizPassoMontano as PosizPassoMontano
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizPalazzoDiRod as PosizPalazzoDiRod
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizTunnelDiRod as PosizTunnelDiRod
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCavernaImpo as PosizCavernaImpo
import Codice.SettaggiLivelli.EventiPerZona.EventiSogno as EventiSogno
import Codice.SettaggiLivelli.EventiPerZona.EventiCasa as EventiCasa
import Codice.SettaggiLivelli.EventiPerZona.EventiForestaCadetta as EventiForestaCadetta
import Codice.SettaggiLivelli.EventiPerZona.EventiStradaPerCitta as EventiStradaPerCitta
import Codice.SettaggiLivelli.EventiPerZona.EventiCitta as EventiCitta
import Codice.SettaggiLivelli.EventiPerZona.EventiCasaUfficiale as EventiCasaUfficiale
import Codice.SettaggiLivelli.EventiPerZona.EventiBiblioteca as EventiBiblioteca
import Codice.SettaggiLivelli.EventiPerZona.EventiStradaPerSelvaArida as EventiStradaPerSelvaArida
import Codice.SettaggiLivelli.EventiPerZona.EventiSelvaArida as EventiSelvaArida
import Codice.SettaggiLivelli.EventiPerZona.EventiAvampostoDiRod as EventiAvampostoDiRod
import Codice.SettaggiLivelli.EventiPerZona.EventiLabirinto as EventiLabirinto
import Codice.SettaggiLivelli.EventiPerZona.EventiEsternoCastello as EventiEsternoCastello
import Codice.SettaggiLivelli.EventiPerZona.EventiInternoCastello as EventiInternoCastello
import Codice.SettaggiLivelli.EventiPerZona.EventiScorciatoiaLabirinto as EventiScorciatoiaLabirinto
import Codice.SettaggiLivelli.EventiPerZona.EventiStradaPerPassoMontano as EventiStradaPerPassoMontano
import Codice.SettaggiLivelli.EventiPerZona.EventiPassoMontano as EventiPassoMontano
import Codice.SettaggiLivelli.EventiPerZona.EventiPalazzoDiRod as EventiPalazzoDiRod
import Codice.SettaggiLivelli.EventiPerZona.EventiTunnelDiRod as EventiTunnelDiRod
import Codice.SettaggiLivelli.EventiPerZona.EventiCavernaImpo as EventiCavernaImpo


def caricaNemiciEPersonaggi(avanzamentoStoria, stanza, stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi, listaPersonaggi, cofanetti):
    if stanzaVecchia != 0 and ((stanza in GlobalGameVar.vetStanzePacifiche) or (stanza not in GlobalGameVar.vetStanzePacifiche and stanzaVecchia in GlobalGameVar.vetStanzePacifiche)):
        listaNemiciTotali = []
        listaPersonaggiTotali = []
        stanzeGiaVisitate = []

    listaNemici = []
    if not stanza in stanzeGiaVisitate:
        if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
            listaNemiciTotali, listaNemici = PosizSogno.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
            listaNemiciTotali, listaNemici = PosizCasaHansSara.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            listaNemiciTotali, listaNemici = PosizForestaCadetta.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            listaNemiciTotali, listaNemici = PosizStradaPerCitta.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
            listaNemiciTotali, listaNemici = PosizCitta.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            listaNemiciTotali, listaNemici = PosizCasaUfficiale.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
            listaNemiciTotali, listaNemici = PosizBiblioteca.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
            listaNemiciTotali, listaNemici = PosizStradaPerSelvaArida.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
            listaNemiciTotali, listaNemici = PosizSelvaArida.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
            listaNemiciTotali, listaNemici = PosizAvampostoDiRod.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
            listaNemiciTotali, listaNemici = PosizLabirinto.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]:
            listaNemiciTotali, listaNemici = PosizEsternoCastello.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
            listaNemiciTotali, listaNemici = PosizInternoCastello.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
            listaNemiciTotali, listaNemici = PosizScorciatoiaLabirinto.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
            listaNemiciTotali, listaNemici = PosizStradaPerPassoMontano.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
            listaNemiciTotali, listaNemici = PosizPassoMontano.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
            listaNemiciTotali, listaNemici = PosizPalazzoDiRod.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
            listaNemiciTotali, listaNemici = PosizTunnelDiRod.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["caverna1"] <= stanza <= GlobalGameVar.dictStanze["caverna17"]:
            listaNemiciTotali, listaNemici = PosizCavernaImpo.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
    else:
        for nemico in listaNemiciTotali:
            if nemico.stanzaDiAppartenenza == stanza:
                listaNemici.append(nemico)

    # aggiorno il vettore listaAvanzamentoDialoghi per i personaggi della stanza precedente
    for personaggio in listaPersonaggi:
        personaggioPresente = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                personaggioPresente = True
                break
            i += 2
        if not personaggioPresente:
            listaAvanzamentoDialoghi.append(personaggio.tipoId)
            listaAvanzamentoDialoghi.append(personaggio.avanzamentoDialogo)

    listaPersonaggi = []
    if not stanza in stanzeGiaVisitate:
        if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
            listaPersonaggiTotali, listaPersonaggi = PosizSogno.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCasaHansSara.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            listaPersonaggiTotali, listaPersonaggi = PosizForestaCadetta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizStradaPerCitta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCitta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCasaUfficiale.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizBiblioteca.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
            listaPersonaggiTotali, listaPersonaggi = PosizStradaPerSelvaArida.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
            listaPersonaggiTotali, listaPersonaggi = PosizSelvaArida.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizAvampostoDiRod.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
            listaPersonaggiTotali, listaPersonaggi = PosizLabirinto.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]:
            listaPersonaggiTotali, listaPersonaggi = PosizEsternoCastello.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
            listaPersonaggiTotali, listaPersonaggi = PosizInternoCastello.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
            listaPersonaggiTotali, listaPersonaggi = PosizScorciatoiaLabirinto.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
            listaPersonaggiTotali, listaPersonaggi = PosizStradaPerPassoMontano.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
            listaPersonaggiTotali, listaPersonaggi = PosizPassoMontano.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
            listaPersonaggiTotali, listaPersonaggi = PosizPalazzoDiRod.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizTunnelDiRod.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        elif GlobalGameVar.dictStanze["caverna1"] <= stanza <= GlobalGameVar.dictStanze["caverna17"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCavernaImpo.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi)
        # metto i personaggi-cofanetto per quando usi Rod
        if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            i = 0
            while i < len(cofanetti):
                if cofanetti[i + 3]:
                    nomeOggetto = "OggettoDictCofanettoAperto-0"
                else:
                    nomeOggetto = "OggettoDictCofanettoChiuso-0"
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(cofanetti[i + 1], cofanetti[i + 2], "s", nomeOggetto, stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                i += 4
    else:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == stanza:
                listaPersonaggi.append(personaggio)

    # aggiorno il vettore listaAvanzamentoDialoghi per i personaggi della stanza attuale
    for personaggio in listaPersonaggi:
        personaggioPresente = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                personaggioPresente = True
                break
            i += 2
        if not personaggioPresente:
            listaAvanzamentoDialoghi.append(personaggio.tipoId)
            listaAvanzamentoDialoghi.append(personaggio.avanzamentoDialogo)

    if not stanza in stanzeGiaVisitate:
        stanzeGiaVisitate.append(stanza)

    # eccezioni col tempo bloccato
    if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        # trasformo i nemici in personaggi se il tempo è bloccato (eccetto quelli nella caverna e nel vulcano)
        for nemico in listaNemici:
            if nemico.stanzaDiAppartenenza < GlobalGameVar.dictStanze["caverna1"]:
                personaggio = PersonaggioObj.PersonaggioObj(nemico.x, nemico.y, nemico.direzione, nemico.tipo + "-0", stanza, avanzamentoStoria, nemico.percorso)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        i = len(listaNemici) - 1
        while i >= 0:
            if listaNemici[i].stanzaDiAppartenenza < GlobalGameVar.dictStanze["caverna1"]:
                del listaNemici[i]
            i -= 1
        i = len(listaNemiciTotali) - 1
        while i >= 0:
            if listaNemiciTotali[i].stanzaDiAppartenenza < GlobalGameVar.dictStanze["caverna1"]:
                del listaNemiciTotali[i]
            i -= 1
        # cancello il percorso dei personaggi se il tempo è bloccato
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza < GlobalGameVar.dictStanze["caverna1"]:
                personaggio.percorso = []
                personaggio.numeroMovimento = 0
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza < GlobalGameVar.dictStanze["caverna1"]:
                personaggio.percorso = []
                personaggio.numeroMovimento = 0
    # eccezioni per caverna impo
    if GlobalGameVar.dictStanze["caverna1"] <= stanza <= GlobalGameVar.dictStanze["caverna17"]:
        for nemico in listaNemici:
            nemico.x, nemico.y = nemico.posizioneOriginale
            nemico.vx, nemico.vy = nemico.posizioneOriginale
            nemico.vita = nemico.vitaTotale
            nemico.avvelenato = False
            nemico.appiccicato = False
            nemico.triggerato = False
            nemico.obbiettivo = ["", 0, 0, []]
            nemico.xPosizioneUltimoBersaglio = False
            nemico.yPosizioneUltimoBersaglio = False
            nemico.numeroMovimento = False
        for nemico in listaNemiciTotali:
            nemico.x, nemico.y = nemico.posizioneOriginale
            nemico.vx, nemico.vy = nemico.posizioneOriginale
            nemico.vita = nemico.vitaTotale
            nemico.avvelenato = False
            nemico.appiccicato = False
            nemico.triggerato = False
            nemico.obbiettivo = ["", 0, 0, []]
            nemico.xPosizioneUltimoBersaglio = False
            nemico.yPosizioneUltimoBersaglio = False
            nemico.numeroMovimento = False

    return listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi


def gestisciEventiStoria(avanzamentoStoria, stanza, npers, x, y, rx, ry, nrob, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, canzone, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire, listaNemiciSotterrati):
    avanzamentoStoriaPreEventi = avanzamentoStoria
    if impossibileAprirePorta:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiSogno.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiCasa.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiForestaCadetta.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiStradaPerCitta.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiCitta.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiCasaUfficiale.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiBiblioteca.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiStradaPerSelvaArida.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiSelvaArida.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiAvampostoDiRod.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiLabirinto.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiEsternoCastello.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiInternoCastello.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiScorciatoiaLabirinto.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiStradaPerPassoMontano.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiPassoMontano.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiPalazzoDiRod.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiTunnelDiRod.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)
    elif GlobalGameVar.dictStanze["caverna1"] <= stanza <= GlobalGameVar.dictStanze["caverna17"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire = EventiCavernaImpo.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire)

    # elimino i personaggi-oggetto dei cadaveri sotterrati
    sotterratoCadaveri = False
    i = len(listaPersonaggi) - 1
    while i >= 0:
        personaggio = listaPersonaggi[i]
        if personaggio.tipo.startswith("OggettoDictCadavere") and not personaggio.tipo.startswith("OggettoDictCadavereSoldatoCastello") and personaggio.avanzamentoDialogo >= 1:
            sotterratoCadaveri = True
            casellaGiaSotterrata = False
            for nemicoSotterrato in listaNemiciSotterrati:
                if nemicoSotterrato[0] == personaggio.x and nemicoSotterrato[1] == personaggio.y:
                    casellaGiaSotterrata = True
                    break
            if not casellaGiaSotterrata:
                listaNemiciSotterrati.append([personaggio.x, personaggio.y])
            listaPersonaggi.remove(personaggio)
            if personaggio in listaPersonaggiTotali:
                listaPersonaggiTotali.remove(personaggio)
        i -= 1
    if sotterratoCadaveri:
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScavareBreve)
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        caricaTutto = True

    evitaAvanzamentoTurno = False
    if caricaTutto or avanzamentoStoriaPreEventi != avanzamentoStoria:
        evitaAvanzamentoTurno = True
        bottoneDown = False

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, evitaAvanzamentoTurno, avanzaManualmentePercorsoDaEseguire, listaNemiciSotterrati
