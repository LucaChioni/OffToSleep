# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


def settaImgMappa(avanzamentoStoria, imgMappa, imgMappaZoom):
    imgDaUsare = GlobalGameVar.imgMappaAttuale
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCasa"]:
        imgDaUsare = "mappaCasa"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaForestaCadetta"]:
        imgDaUsare = "mappaForestaCadetta"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCittà"]:
        imgDaUsare = "mappaCittà"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaSelvaArida"]:
        imgDaUsare = "mappaSelvaArida"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaAvampostoDiRod"]:
        imgDaUsare = "mappaAvampostoDiRod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLabirinto"]:
        imgDaUsare = "mappaLabirinto"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLabirintoRisolto"]:
        imgDaUsare = "mappaLabirintoRisolto"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCastello"]:
        imgDaUsare = "mappaCastello"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaScorciatoiaLabirinto"]:
        imgDaUsare = "mappaScorciatoiaLabirinto"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPassoMontano"]:
        imgDaUsare = "mappaPassoMontano"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPalazzoDiRod"]:
        imgDaUsare = "mappaPalazzoDiRod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCaverna"]:
        imgDaUsare = "mappaCaverna"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaVulcano"]:
        imgDaUsare = "mappaVulcano"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod"]:
        imgDaUsare = "mappaTunnelDiRod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelSubacqueo"]:
        imgDaUsare = "mappaTunnelSubacqueo"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLaboratorio"]:
        imgDaUsare = "mappaLaboratorio"

    if imgDaUsare != GlobalGameVar.imgMappaAttuale:
        GlobalGameVar.imgMappaAttuale = imgDaUsare
        if imgDaUsare == "mappaCasa":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaForestaCadetta":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaCittà":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaSelvaArida":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaAvampostoDiRod":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaLabirinto":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaLabirintoRisolto":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaCastello":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaScorciatoiaLabirinto":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaPassoMontano":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaPalazzoDiRod":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaCaverna":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaVulcano":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaTunnelDiRod":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaTunnelSubacqueo":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaLaboratorio":
            imgMappa = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu15.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            imgMappaZoom = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu15.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)

    return imgMappa, imgMappaZoom


def definisciImgOggetti(tipo):
    disegnaImg = False
    numImg = 1
    numImgDialogo = 1
    nomeImgDialogo = ["Vuota"]

    if tipo == "OggettoLettoSara":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 3
        nomeImgDialogo = ["SaraDormienteDialogo1", "SaraDormienteDialogo2", "Vuota"]
    if tipo == "OggettoComodinoSara":
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
    if tipo == "OggettoSaraSedutaBiblioteca":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoTavoloMappaLabirinto":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoEnigmaLabirinto":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoPappaLibroSonoroMercante":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["PappaLibroSonoroMercanteDialogo"]
    if tipo.startswith("OggettoCassaMercante"):
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoSaraSedutaCastello":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]

    return disegnaImg, numImg, numImgDialogo, nomeImgDialogo


def impostaImgOggettoDaUsare(tipo, avanzamentoStoria, avanzamentoDialogo):
    numImgAttuale = 0

    if tipo == "OggettoComodinoSara":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"]:
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
    if tipo == "OggettoTavoloMappaLabirinto":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["messaMappaLabirintoSulTavolo"]:
            numImgAttuale = 1

    return numImgAttuale


def impostaImgOggettoDialogoDaUsare(tipo, avanzamentoStoria, avanzamentoDialogo):
    numImgAttualeDialogo = 0

    if tipo == "OggettoLettoSara":
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
