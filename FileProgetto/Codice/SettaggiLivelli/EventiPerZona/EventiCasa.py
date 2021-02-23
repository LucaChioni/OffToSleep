# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        screen = GlobalHWVar.schermo.copy().convert()

        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoLettoLucy", stanza, avanzamentoStoria, False)
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonno4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate
