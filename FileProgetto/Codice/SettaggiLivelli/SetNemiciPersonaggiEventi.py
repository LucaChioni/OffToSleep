# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizSogno as PosizSogno
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCasa as PosizCasaHansLucy
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizForestaCadetta as PosizForestaCadetta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizStradaPerCitta as PosizStradaPerCitta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCasaUfficiale as PosizCasaUfficiale
import Codice.SettaggiLivelli.EventiPerZona.EventiSogno as EventiSogno
import Codice.SettaggiLivelli.EventiPerZona.EventiCasa as EventiCasa
import Codice.SettaggiLivelli.EventiPerZona.EventiForestaCadetta as EventiForestaCadetta
import Codice.SettaggiLivelli.EventiPerZona.EventiStradaPerCitta as EventiStradaPerCitta
import Codice.SettaggiLivelli.EventiPerZona.EventiCasaUfficiale as EventiCasaUfficiale


def caricaNemiciEPersonaggi(avanzamentoStoria, stanza, stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi, listaPersonaggi):
    if stanzaVecchia != 0 and ((stanza in GlobalGameVar.vetStanzePacifiche) or (stanza not in GlobalGameVar.vetStanzePacifiche and stanzaVecchia in GlobalGameVar.vetStanzePacifiche)):
        listaNemiciTotali = []
        listaPersonaggiTotali = []
        stanzeGiaVisitate = []

    listaNemici = []
    if not stanza in stanzeGiaVisitate:
        if GlobalGameVar.dictStanze["sognoLucy1"] <= stanza <= GlobalGameVar.dictStanze["sognoLucy4"]:
            listaNemiciTotali, listaNemici = PosizSogno.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
            listaNemiciTotali, listaNemici = PosizCasaHansLucy.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            listaNemiciTotali, listaNemici = PosizForestaCadetta.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            listaNemiciTotali, listaNemici = PosizStradaPerCitta.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            listaNemiciTotali, listaNemici = PosizCasaUfficiale.setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria)
    else:
        for nemico in listaNemiciTotali:
            if nemico.stanzaDiAppartenenza == stanza:
                listaNemici.append(nemico)

    # aggiorno il vettore listaAvanzamentoDialoghi per i personaggi della stanza precedente
    for personaggio in listaPersonaggi:
        personaggioPresente = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if personaggio.tipo == listaAvanzamentoDialoghi[i]:
                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                personaggioPresente = True
                break
            i += 2
        if not personaggioPresente:
            listaAvanzamentoDialoghi.append(personaggio.tipo)
            listaAvanzamentoDialoghi.append(personaggio.avanzamentoDialogo)

    listaPersonaggi = []
    if not stanza in stanzeGiaVisitate:
        if GlobalGameVar.dictStanze["sognoLucy1"] <= stanza <= GlobalGameVar.dictStanze["sognoLucy4"]:
            listaPersonaggiTotali, listaPersonaggi = PosizSogno.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCasaHansLucy.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            listaPersonaggiTotali, listaPersonaggi = PosizForestaCadetta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizStradaPerCitta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCasaUfficiale.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
    else:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == stanza:
                listaPersonaggi.append(personaggio)

    # aggiorno il vettore listaAvanzamentoDialoghi per i personaggi della stanza attuale
    for personaggio in listaPersonaggi:
        personaggioPresente = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if personaggio.tipo == listaAvanzamentoDialoghi[i]:
                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                personaggioPresente = True
                break
            i += 2
        if not personaggioPresente:
            listaAvanzamentoDialoghi.append(personaggio.tipo)
            listaAvanzamentoDialoghi.append(personaggio.avanzamentoDialogo)

    if not stanza in stanzeGiaVisitate:
        stanzeGiaVisitate.append(stanza)

    return listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi


def gestisciEventiStoria(avanzamentoStoria, stanza, npers, x, y, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, canzone, avanzaIlTurnoSenzaMuoverti):
    if impossibileAprirePorta:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    if GlobalGameVar.dictStanze["sognoLucy1"] <= stanza <= GlobalGameVar.dictStanze["sognoLucy4"]:
        avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti = EventiSogno.gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti)
    elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
        avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti = EventiCasa.gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti = EventiForestaCadetta.gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti = EventiStradaPerCitta.gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
        avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti = EventiCasaUfficiale.gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti)

    if caricaTutto:
        bottoneDown = False
    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti
