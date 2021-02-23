# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        screen = GlobalHWVar.schermo.copy().convert()

        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)

        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.canaleSoundCanzone.set_volume(0)
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        i = 0
        while i < GlobalHWVar.volumeCanzoni:
            GlobalHWVar.canaleSoundCanzone.set_volume(i)
            i += GlobalHWVar.volumeCanzoni / 10
            pygame.time.wait(30)
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoConDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        padreArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 28 and personaggio.y == GlobalHWVar.gpy * 11:
                    padreArrivato = True
                break

        if padreArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioBagnoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        dati[6] = 0
        dati[7] = 0
        dati[8] = 0
        dati[128] = 0
        dati[129] = 0
        dati[130] = 0
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        aggiornaImgEquip = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreCambioPerCenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and personaggio.tipo == "PadreUfficialeServizio":
                listaPersonaggiTotali.remove(personaggio)
                break
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate
