# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def definisciImgOggetti(tipo):
    disegnaImg = False
    numImg = 1
    numImgDialogo = 1
    nomeImgDialogo = ["Vuota"]

    if tipo == "OggettoLettoLucy":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 3
        nomeImgDialogo = ["LucyDormienteDialogo1", "LucyDormienteDialogo2", "Vuota"]
    if tipo == "OggettoComodinoLucy":
        disegnaImg = True
        numImg = 4
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoSiepe":
        disegnaImg = True
        numImg = 3
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoFuoco":
        disegnaImg = True
        numImg = 3
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoCibo":
        disegnaImg = True
        numImg = 3
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoMucchioLegna":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo.startswith("OggettoLegna"):
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoCinghiale":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["CinghialeDialogo"]
    if tipo == "OggettoPersonaCadavereSam":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 2
        nomeImgDialogo = ["Vuota", "FiglioUfficialeCadavereDialogo"]
    if tipo == "OggettoTombaSam":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoMadreUfficialeSeduta":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoPadreUfficialeSeduto":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoPersonaCittadino3Cadavere":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Cittadino3CadavereDialogo"]
    if tipo == "OggettoPersonaCittadino1Cadavere":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Cittadino1CadavereDialogo"]
    if tipo == "OggettoAssistBiblioteca":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["AssistBibliotecaDialogo"]
    if tipo == "OggettoLibreriaRegistri":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoRegistroBiblioteca":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoVomito":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoMocio":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoLucySeduta":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoTavoloEnigmaLabirinto":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]

    return disegnaImg, numImg, numImgDialogo, nomeImgDialogo


def impostaImgOggettoDaUsare(tipo, avanzamentoStoria, avanzamentoDialogo):
    numImgAttuale = 0

    if tipo == "OggettoComodinoLucy":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
            numImgAttuale = 3
    if tipo == "OggettoSiepe":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            numImgAttuale = 2
    if tipo == "OggettoFuoco":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttuale = 2
    if tipo == "OggettoCibo":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            numImgAttuale = 2
    if tipo == "OggettoMucchioLegna":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["legnaDepositata"]:
            numImgAttuale = 1
    if tipo.startswith("OggettoLegna"):
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"] or avanzamentoDialogo == 1:
            numImgAttuale = 1
    if tipo == "OggettoTombaSam":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            numImgAttuale = 1
    if tipo == "OggettoLibreriaRegistri":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["toltoRegistroBibliotecaDallaLibreria"]:
            numImgAttuale = 1
    if tipo == "OggettoRegistroBiblioteca":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["messoRegistroBibliotecaSullaScrivania"]:
            numImgAttuale = 1
    if tipo == "OggettoVomito":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
            numImgAttuale = 1
    if tipo == "OggettoTavoloEnigmaLabirinto":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["messaMappaLabirintoSulTavolo"]:
            numImgAttuale = 1

    return numImgAttuale


def impostaImgOggettoDialogoDaUsare(tipo, avanzamentoStoria, avanzamentoDialogo):
    numImgAttualeDialogo = 0

    if tipo == "OggettoLettoLucy":
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
            numImgAttualeDialogo = 0
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 2
    if tipo == "OggettoPersonaCadavereSam":
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
            numImgAttualeDialogo = 0
        else:
            numImgAttualeDialogo = 1

    return numImgAttualeDialogo
