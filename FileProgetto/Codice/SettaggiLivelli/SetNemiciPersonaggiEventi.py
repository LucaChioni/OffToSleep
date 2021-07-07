# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizSogno as PosizSogno
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCasa as PosizCasaHansLucy
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizForestaCadetta as PosizForestaCadetta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizStradaPerCitta as PosizStradaPerCitta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCitta as PosizCitta
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizCasaUfficiale as PosizCasaUfficiale
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizBiblioteca as PosizBiblioteca
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizStradaPerSelvaArida as PosizStradaPerSelvaArida
import Codice.SettaggiLivelli.PosizNemiciPersonaggiPerZona.PosizSelvaArida as PosizSelvaArida
import Codice.SettaggiLivelli.EventiPerZona.EventiSogno as EventiSogno
import Codice.SettaggiLivelli.EventiPerZona.EventiCasa as EventiCasa
import Codice.SettaggiLivelli.EventiPerZona.EventiForestaCadetta as EventiForestaCadetta
import Codice.SettaggiLivelli.EventiPerZona.EventiStradaPerCitta as EventiStradaPerCitta
import Codice.SettaggiLivelli.EventiPerZona.EventiCitta as EventiCitta
import Codice.SettaggiLivelli.EventiPerZona.EventiCasaUfficiale as EventiCasaUfficiale
import Codice.SettaggiLivelli.EventiPerZona.EventiBiblioteca as EventiBiblioteca
import Codice.SettaggiLivelli.EventiPerZona.EventiStradaPerSelvaArida as EventiStradaPerSelvaArida
import Codice.SettaggiLivelli.EventiPerZona.EventiSelvaArida as EventiSelvaArida


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
        if GlobalGameVar.dictStanze["sognoLucy1"] <= stanza <= GlobalGameVar.dictStanze["sognoLucy4"]:
            listaPersonaggiTotali, listaPersonaggi = PosizSogno.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCasaHansLucy.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            listaPersonaggiTotali, listaPersonaggi = PosizForestaCadetta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizStradaPerCitta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCitta.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizCasaUfficiale.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
            listaPersonaggiTotali, listaPersonaggi = PosizBiblioteca.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
            listaPersonaggiTotali, listaPersonaggi = PosizStradaPerSelvaArida.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
            listaPersonaggiTotali, listaPersonaggi = PosizSelvaArida.setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria)
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

    return listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi


def gestisciEventiStoria(avanzamentoStoria, stanza, npers, x, y, rx, ry, nrob, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, canzone, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse):
    if impossibileAprirePorta:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    if GlobalGameVar.dictStanze["sognoLucy1"] <= stanza <= GlobalGameVar.dictStanze["sognoLucy4"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiSogno.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiCasa.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiForestaCadetta.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiStradaPerCitta.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiCitta.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiCasaUfficiale.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiBiblioteca.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiStradaPerSelvaArida.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
        x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire = EventiSelvaArida.gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse)

    if caricaTutto:
        bottoneDown = False
    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire
