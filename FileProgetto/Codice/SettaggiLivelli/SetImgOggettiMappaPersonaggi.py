# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


def settaImgMappa(avanzamentoStoria):
    imgDaUsare = GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgMappaAttuale"]
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
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod"]:
        imgDaUsare = "mappaTunnelDiRod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaVistoVulcano"]:
        imgDaUsare = "mappaVistoVulcano"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCaverna"]:
        imgDaUsare = "mappaCaverna"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaVulcano"]:
        imgDaUsare = "mappaVulcano"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelSubacqueo"]:
        imgDaUsare = "mappaTunnelSubacqueo"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLaboratorio"]:
        imgDaUsare = "mappaLaboratorio"

    if imgDaUsare != GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgMappaAttuale"]:
        GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgMappaAttuale"] = imgDaUsare
        if imgDaUsare == "mappaCasa":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaForestaCadetta":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaCittà":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaSelvaArida":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaAvampostoDiRod":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaLabirinto":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaLabirintoRisolto":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaCastello":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaScorciatoiaLabirinto":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaPassoMontano":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaPalazzoDiRod":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaTunnelDiRod":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaVistoVulcano":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaCaverna":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaVulcano":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaTunnelSubacqueo":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu15.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu15.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)
        elif imgDaUsare == "mappaLaboratorio":
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu16.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False, True)
            GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"] = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu16.png", GlobalHWVar.gpx * 66, GlobalHWVar.gpy * 45, False, True)


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
        numImg = 4
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
    if tipo == "OggettoTavoloVuotoCastelloA":
        disegnaImg = True
        numImg = 3
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoTavoloVuotoCastelloB":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo.startswith("OggettoDictCadavereSoldato"):
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["OggettoDictCadavereSoldatoDialogo"]
    if tipo == "OggettoSaraNelLago":
        disegnaImg = True
        numImg = 5
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo.startswith("OggettoDictCofanetto"):
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
        if GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            numImgAttuale = 3
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
    if tipo == "OggettoTavoloVuotoCastelloA":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["messoStrumentiSulTavoloDiNeil"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            numImgAttuale = 1
    if tipo == "OggettoTavoloVuotoCastelloB":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["rimossoImpoMessoSulTavoloDopoConsegnaStrumenti"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cliccatoImpoPietraPerFuggireDaNeilConImpo"]:
            numImgAttuale = 0
    if tipo == "OggettoSaraNelLago":
        if GlobalGameVar.armaturaIndossata == 0 and not GlobalGameVar.cambiataAlCastello[0]:
            numImgAttuale = 0
        if GlobalGameVar.armaturaIndossata == 0 and GlobalGameVar.cambiataAlCastello[0]:
            numImgAttuale = 1
        if GlobalGameVar.armaturaIndossata == 1:
            numImgAttuale = 2
        if GlobalGameVar.armaturaIndossata == 2:
            numImgAttuale = 3
        if GlobalGameVar.armaturaIndossata == 3:
            numImgAttuale = 4

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


def setImgDialogoProtagonista(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        GlobalGameVar.nomePersonaggioDialoghi = "Hans"
        imgDaUsare = "FratelloMaggioreDialogo"
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] or GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
        GlobalGameVar.nomePersonaggioDialoghi = "Sara"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            imgDaUsare = "Sara1Dialogo"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            imgDaUsare = "SaraAssonnataDialogo"
        elif GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà7"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            imgDaUsare = "SaraScossaDialogo"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDiPensareASceltaPassataNelDialogoBibliotecario"]:
            imgDaUsare = "SaraOcchiChiusiDialogo"
        elif GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgDaUsare = "SaraAssonnataDialogoPostCenaCastello"
            else:
                imgDaUsare = "SaraAssonnataCastelloDialogoPostCenaCastello"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgDaUsare = "SaraAssonnataDialogo"
            else:
                imgDaUsare = "SaraAssonnataCastelloDialogo"
        elif GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgDaUsare = "SaraScossaDialogo"
            else:
                imgDaUsare = "SaraScossaCastelloDialogo"
        elif not GlobalGameVar.cambiataAlCastello[0]:
            imgDaUsare = "Sara2Dialogo"
        else:
            imgDaUsare = "Sara3Dialogo"
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        GlobalGameVar.nomePersonaggioDialoghi = "Rod"
        imgDaUsare = "RodDialogo"
    else:
        GlobalGameVar.nomePersonaggioDialoghi = "Sara"
        imgDaUsare = "Sara3Dialogo"

    if imgDaUsare != GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaDialogoAttuale"]:
        GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaDialogoAttuale"] = imgDaUsare
        GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgPersonaggioDialoghi"] = CaricaFileProgetto.loadImage('Risorse/Immagini/DecorazioniMenu/Dialoghi/' + imgDaUsare + '.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)


def setImgMenuStartProtagonista(avanzamentoStoria):
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        imgDaUsare = "Sara1GrafMenu"
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        imgDaUsare = "FratelloMaggioreGrafMenu"
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        imgDaUsare = "Sara1GrafMenu"
    elif GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"]:
        imgDaUsare = "SaraSconvoltaGrafMenu"
    elif GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            imgDaUsare = "SaraAssonnataPostCenaCastelloGrafMenu"
        else:
            imgDaUsare = "SaraAssonnataCastelloPostCenaCastelloGrafMenu"
    elif GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            imgDaUsare = "SaraSconvoltaGrafMenu"
        else:
            imgDaUsare = "SaraSconvoltaCastelloGrafMenu"
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            imgDaUsare = "Sara2GrafMenu"
        else:
            imgDaUsare = "Sara3GrafMenu"
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        imgDaUsare = "MercanteGrafMenuStart"
    else:
        imgDaUsare = "Sara3GrafMenu"

    if imgDaUsare != GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaStartAttuale"]:
        GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaStartAttuale"] = imgDaUsare
        GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgPersonaggioStart"] = CaricaFileProgetto.loadImage('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/' + imgDaUsare + '.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)


def setImgMenuOggettiProtagonista(avanzamentoStoria):
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        imgDaUsare = "Sara1Menu"
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        imgDaUsare = "FratelloMaggioreMenu"
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        imgDaUsare = "Sara1Menu"
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            imgDaUsare = "Sara2Menu"
        else:
            imgDaUsare = "Sara3Menu"
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        imgDaUsare = "RodMenu"
    else:
        imgDaUsare = "Sara3Menu"

    if imgDaUsare != GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaMenuOggettiAttuale"]:
        GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaMenuOggettiAttuale"] = imgDaUsare
        GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgPersonaggioMenuOggetti"] = CaricaFileProgetto.loadImage('Risorse/Immagini/DecorazioniMenu/' + imgDaUsare + '.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)


def setImgMenuSalvaProtagonista(avanzamentoStoria, abitiCastello):
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        persalva = GlobalImgVar.persoSara1
        persSalvaBraccia = GlobalImgVar.persobSara
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        persalva = GlobalImgVar.persoFraMaggiore
        persSalvaBraccia = GlobalImgVar.persobFraMaggiore
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        persalva = GlobalImgVar.persoSara1
        persSalvaBraccia = GlobalImgVar.persobSara
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
        if not abitiCastello:
            persalva = GlobalImgVar.persoSara2
            persSalvaBraccia = GlobalImgVar.persobSara
        else:
            persalva = GlobalImgVar.persoSara3
            persSalvaBraccia = GlobalImgVar.persobSara
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        persalva = GlobalImgVar.persoRod
        persSalvaBraccia = GlobalImgVar.persobRod
    else:
        persalva = GlobalImgVar.persoSara3
        persSalvaBraccia = GlobalImgVar.persobSara

    return persalva, persSalvaBraccia


def cambiaProtagonista(avanzamentoStoria, personaggioUsato=False):
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        personaggioDaUsare = "Sara1"
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        personaggioDaUsare = "FratelloMaggiore"
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        personaggioDaUsare = "Sara1"
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            personaggioDaUsare = "Sara2"
        else:
            personaggioDaUsare = "Sara3"
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        personaggioDaUsare = "RodGiocabile"
    else:
        personaggioDaUsare = "Sara3"
    if personaggioDaUsare != personaggioUsato:
        GlobalImgVar.persw = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perswb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persa = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persab = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perso = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
        GlobalImgVar.perss = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persob = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
        GlobalImgVar.perssb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persd = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persdb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perssm = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perssmb1 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perssmb2 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persdm = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio2mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persdmb1 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio2movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persdmb2 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio2movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persam = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio3mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persamb1 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio3movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persamb2 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio3movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perswm = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio4mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perswmb1 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio4movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perswmb2 = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio4movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perswmbAttacco = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio4movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persambAttacco = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio3movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.perssmbAttacco = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio1movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persdmbAttacco = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/Personaggio2movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persmbDifesa = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/PersonaggiomovbDifesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalImgVar.persAvvele = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/' + personaggioDaUsare + '/PersonaggioAvvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)


def setImgMercanteMenu(avanzamentoStoria, stanza):
    interlocutore = "Rod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        interlocutore = "Sara"
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] and stanza == GlobalGameVar.dictStanze["città5"]:
        interlocutore = "Pappagallo"
    elif stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        interlocutore = "Pappagallo"

    return interlocutore
