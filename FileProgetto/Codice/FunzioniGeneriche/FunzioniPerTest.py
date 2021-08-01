# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc


def testOstacoli(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria, entrateStanza):
    caselleNonVisibili, colcoInCasellaVista = GenericFunc.scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria, escludiOggettiBassi=True, vetPartenze=entrateStanza)
    i = 0
    while i < len(caselleNonVisibili):
        if caselleNonVisibili[i + 2]:
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.gialloCarta, (caselleNonVisibili[i] + GlobalHWVar.gpx * 0.3, caselleNonVisibili[i + 1] + GlobalHWVar.gpy * 0.3, GlobalHWVar.gpx * 0.4, GlobalHWVar.gpy * 0.4))
        i += 3
    GlobalHWVar.aggiornaSchermo()
