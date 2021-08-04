# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc


def testOstacoli(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria, entrateStanza):
    caselleNonPercorribili, colcoInCasellaVista = GenericFunc.scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria, escludiOggettiBassi=True, vetPartenze=entrateStanza)
    i = 0
    while i < len(caselleNonPercorribili):
        if caselleNonPercorribili[i + 2]:
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.gialloCarta, (caselleNonPercorribili[i] + GlobalHWVar.gpx * 0.3, caselleNonPercorribili[i + 1] + GlobalHWVar.gpy * 0.3, GlobalHWVar.gpx * 0.4, GlobalHWVar.gpy * 0.4))
        i += 3
    caselleNonVisibili, colcoInCasellaVista = GenericFunc.scopriCaselleViste(x, y, rx, ry, stanza, porte, cofanetti, avanzamentoStoria, escludiOggettiBassi=False, vetPartenze=entrateStanza)
    i = 0
    while i < len(caselleNonVisibili):
        if caselleNonVisibili[i + 2]:
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.rosso, (caselleNonVisibili[i] + GlobalHWVar.gpx * 0.3, caselleNonVisibili[i + 1] + GlobalHWVar.gpy * 0.3, GlobalHWVar.gpx * 0.4, GlobalHWVar.gpy * 0.4))
        i += 3
    GlobalHWVar.aggiornaSchermo()
