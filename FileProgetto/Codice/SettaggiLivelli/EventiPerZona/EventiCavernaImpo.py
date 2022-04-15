# -*- coding: utf-8 -*-

import random
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello5"] and stanza == GlobalGameVar.dictStanze["caverna1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    # se un nemico ti vede, tutti sanno dove sei
    listaObiettiviVisti = []
    for nemico in listaNemici:
        if nemico.inCasellaVista and nemico.obbiettivo[0] != "":
            listaObiettiviVisti.append([nemico.obbiettivo[1], nemico.obbiettivo[2]])
    if len(listaObiettiviVisti) > 0:
        for nemico in listaNemici:
            if nemico.inCasellaVista and nemico.obbiettivo[0] == "":
                primoObiettivo = True
                for obiettivoVisto in listaObiettiviVisti:
                    if primoObiettivo:
                        nemico.xPosizioneUltimoBersaglio = obiettivoVisto[0]
                        nemico.yPosizioneUltimoBersaglio = obiettivoVisto[1]
                        primoObiettivo = False
                    elif abs(nemico.x - obiettivoVisto[0]) + abs(nemico.y - obiettivoVisto[1]) < abs(nemico.x - nemico.xPosizioneUltimoBersaglio) + abs(nemico.y - nemico.yPosizioneUltimoBersaglio):
                        nemico.xPosizioneUltimoBersaglio = obiettivoVisto[0]
                        nemico.yPosizioneUltimoBersaglio = obiettivoVisto[1]

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
