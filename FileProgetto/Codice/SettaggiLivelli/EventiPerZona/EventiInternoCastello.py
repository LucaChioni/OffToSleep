# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, equipaggiamentoIndossato):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello5"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"] and personaggio.tipoId == "ServoLancia-3":
                if personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 5 and personaggio.direzione == "w":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaSiAccorgeCheNonLoSegui"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-3", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoServoLanciaEntrataNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"] and personaggio.tipoId == "ServoLancia-3":
                if personaggio.x == GlobalHWVar.gpx * 8 and personaggio.y == GlobalHWVar.gpy * 15:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"] and personaggio.tipoId == "ServoLancia-3":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"] and personaggio.tipoId == "ServoLancia-3":
                    listaPersonaggi.remove(personaggio)
                    break
            carim = True
            caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire
