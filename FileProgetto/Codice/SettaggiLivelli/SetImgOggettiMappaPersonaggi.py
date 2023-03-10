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
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCittÃ "]:
        imgDaUsare = "mappaCittÃ "
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
        elif imgDaUsare == "mappaCittÃ ":
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
        numImg = 5
        numImgDialogo = 2
        nomeImgDialogo = ["Vuota", "SaraDuranteOperazioneDialogo"]
    if tipo == "OggettoTavoloVuotoCastelloB":
        disegnaImg = True
        numImg = 3
        numImgDialogo = 2
        nomeImgDialogo = ["Vuota", "SaraDuranteOperazioneDialogo"]
    if tipo.startswith("OggettoDictCadavere"):
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = [tipo[:-1] + "Dialogo"]
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
    if tipo == "OggettoCumuloImpo":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoSaraSdraiata":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoCellaCostruttore":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 2
        nomeImgDialogo = ["Costruttore1Dialogo", "Costruttore2Dialogo"]
    if tipo == "OggettoCellaNeil":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 2
        nomeImgDialogo = ["Vuota", "NeilDialogo"]
    if tipo == "OggettoImpoScarico":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["ImpoScaricoDialogo"]
    if tipo == "OggettoLettoNeilA":
        disegnaImg = True
        numImg = 3
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoLettoNeilB":
        disegnaImg = True
        numImg = 2
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoBibliotecarioCalcolatore":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["BibliotecarioConCascoDialogo"]
    if tipo == "OggettoImpoFermo":
        disegnaImg = True
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["Vuota"]
    if tipo == "OggettoLavandinoCasaDavid":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 3
        nomeImgDialogo = ["Vuota", "SpecchioDialogoSara", "SpecchioDialogoSaraVestitiDavid"]
    if tipo == "OggettoSpecchioCastello":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 6
        nomeImgDialogo = ["SpecchioDialogoSara", "SpecchioDialogoSaraVestitiCastello", "SpecchioDialogoSaraSconvolta", "SpecchioDialogoSaraSconvoltaVestitiCastello", "SpecchioDialogoRod", "SpecchioDialogoSaraResuscitata"]
    if tipo == "OggettoSpecchio":
        disegnaImg = False
        numImg = 1
        numImgDialogo = 1
        nomeImgDialogo = ["SpecchioDialogoSara"]

    return disegnaImg, numImg, numImgDialogo, nomeImgDialogo


def impostaImgOggettoDaUsare(tipo, avanzamentoStoria, avanzamentoDialogo):
    numImgAttuale = 0

    if tipo == "OggettoComodinoSara":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["messoBicchiereConAcquaSulComodino"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
            numImgAttuale = 3
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa2NellaSeraDellInizioDelGioco"]:
            numImgAttuale = 3
    if tipo == "OggettoSiepe":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            numImgAttuale = 2
        if GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            numImgAttuale = 3
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            numImgAttuale = 1
    if tipo == "OggettoFuoco":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            numImgAttuale = 2
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            numImgAttuale = 1
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["colpitoHansDalCinghialeCalcolatore"]:
                numImgAttuale = 2
    if tipo == "OggettoCibo":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            numImgAttuale = 2
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            numImgAttuale = 1
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
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["sdraiataSulTavoloPostRianimazione"]:
            numImgAttuale = 3
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["iniezioneSiringaOperazioneBloccoTempo"]:
            numImgAttuale = 4
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            numImgAttuale = 3
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["alzataDaTavoloPostBloccoTempo"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"]:
            numImgAttuale = 4
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioTemporaleIndietroDi10MinutiInInternoCastello20"]:
            numImgAttuale = 4
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
            numImgAttuale = 1
    if tipo == "OggettoTavoloVuotoCastelloB":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["rimossoImpoMessoSulTavoloDopoConsegnaStrumenti"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cliccatoImpoPietraPerFuggireDaNeilConImpo"]:
            numImgAttuale = 0
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["sdraiataSulTavoloPostRianimazione"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["alzataDaTavoloPostBloccoTempo"]:
            numImgAttuale = 0
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
            numImgAttuale = 0
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioTemporaleIndietroDi10MinutiInInternoCastello20"]:
            numImgAttuale = 2
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
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
    if tipo == "OggettoSaraSdraiata":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["risvegliatoNelVulcano"]:
            numImgAttuale = 1
    if tipo == "OggettoLettoNeilA":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["sdraiatoNeilSulLettoDelLaboratorio"]:
            numImgAttuale = 1
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["chiusoOcchiNeilSulLettoDelLaboratorio"]:
            numImgAttuale = 2
    if tipo == "OggettoLettoNeilB":
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["sdraiatoNeilSulLettoDelLaboratorio"]:
            numImgAttuale = 1

    return numImgAttuale


def impostaImgOggettoDialogoDaUsare(tipo, avanzamentoStoria, avanzamentoDialogo):
    numImgAttualeDialogo = 0

    if tipo == "OggettoLettoSara":
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
            numImgAttualeDialogo = 0
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa2NellaSeraDellInizioDelGioco"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 2
    if tipo == "OggettoPersonaCadavereSam":
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
            numImgAttualeDialogo = 0
        else:
            numImgAttualeDialogo = 1
    if tipo == "OggettoCellaCostruttore":
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 0
    if tipo == "OggettoTavoloVuotoCastelloA":
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
            numImgAttualeDialogo = 1
        elif GlobalGameVar.dictAvanzamentoStoria["inizioViaggioTemporaleIndietroDi10MinutiInInternoCastello20"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 0
    if tipo == "OggettoTavoloVuotoCastelloB":
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
            numImgAttualeDialogo = 1
        elif GlobalGameVar.dictAvanzamentoStoria["inizioViaggioTemporaleIndietroDi10MinutiInInternoCastello20"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 0
    if tipo == "OggettoCellaNeil":
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 0
    if tipo == "OggettoLavandinoCasaDavid":
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            numImgAttualeDialogo = 0
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 2
    if tipo == "OggettoSpecchioCastello":
        if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            numImgAttualeDialogo = 4
        elif GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and not GlobalGameVar.cambiataAlCastello[0]:
            numImgAttualeDialogo = 2
        elif GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and GlobalGameVar.cambiataAlCastello[0]:
            numImgAttualeDialogo = 3
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and not GlobalGameVar.cambiataAlCastello[0]:
            numImgAttualeDialogo = 0
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and GlobalGameVar.cambiataAlCastello[0]:
            numImgAttualeDialogo = 1
        else:
            numImgAttualeDialogo = 5

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
        elif GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittÃ 7"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
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
    elif GlobalGameVar.dictAvanzamentoStoria["iniezioneSiringaOperazioneBloccoTempo"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["apertoOcchiPostdialogoNeilRene1"]:
        GlobalGameVar.nomePersonaggioDialoghi = u"RenÃ©"
        imgDaUsare = "ReneDialogo"
    elif GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogo2RenÃ©NeilPostAvvioSequenzaNelCalcolatore"]:
        GlobalGameVar.nomePersonaggioDialoghi = u"RenÃ©"
        imgDaUsare = "ReneDialogo"
    elif GlobalGameVar.dictAvanzamentoStoria["uscitoRodDalPalazzoPreLancioMissile"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avvioLancioMissileNucleare"]:
        GlobalGameVar.nomePersonaggioDialoghi = u"Rod"
        imgDaUsare = "RodFuturoDialogo"
    elif GlobalGameVar.dictAvanzamentoStoria["arrivataInForestaCadetta5Calcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoHansSamCalcolatore"]:
        GlobalGameVar.nomePersonaggioDialoghi = u"Hans"
        imgDaUsare = "FratelloMaggioreDialogo"
    else:
        GlobalGameVar.nomePersonaggioDialoghi = "Sara"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"]:
            imgDaUsare = "Sara4BendataDialogo"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["voltatoBibliotecarioDopoIlDialogoPostRianimazione"]:
            imgDaUsare = "Sara4Dialogo"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoConImpoPostTempoBloccato"]:
            imgDaUsare = "Sara4ScossaDialogo"
        else:
            imgDaUsare = "Sara4Dialogo"

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
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["voltatoBibliotecarioDopoIlDialogoPostRianimazione"]:
            imgDaUsare = "Sara4GrafMenu"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoConImpoPostTempoBloccato"]:
            imgDaUsare = "Sara4SconvoltaGrafMenu"
        elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            imgDaUsare = "Sara5GrafMenu"
        else:
            imgDaUsare = "Sara4GrafMenu"

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
        imgDaUsare = "Sara4Menu"

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
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        persalva = GlobalImgVar.persoSara5
        persSalvaBraccia = GlobalImgVar.persobSara5
    elif avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fine"]:
        persalva = GlobalImgVar.persoSara6
        persSalvaBraccia = GlobalImgVar.persobSara
    else:
        persalva = GlobalImgVar.persoSara4
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
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        personaggioDaUsare = "Sara5"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["scesoDalCalcolatorePostScopertaFineDelMondo"]:
            personaggioDaUsare = "Sara4"
    else:
        personaggioDaUsare = "Sara4"
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
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] and stanza == GlobalGameVar.dictStanze["cittÃ 5"]:
        interlocutore = "Pappagallo"
    elif stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        interlocutore = "Pappagallo"

    return interlocutore
