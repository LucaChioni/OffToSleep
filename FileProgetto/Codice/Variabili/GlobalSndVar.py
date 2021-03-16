# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


# dichiaro le variabili globali della funzione loadSounds
global selsta
global selind
global spostapun
global selimp
global selezione
global spostaPunBattaglia
global selObbiettivo
global rumoreAttaccoSpada
global rumoreLancioFreccia
global rumoreAttaccoArco
global rumoreParata
global rumorecamminata
global rumorelevelup
global rumoreMorte
global suonoaperturacofanetti
global suonoaperturaporteForesta
global suonochiusuraporteForesta
global suonoaperturaporteCasa
global suonochiusuraporteCasa
global suonoRaccoltaEsca
global suonoRaccoltaMonete
global rumoreAcquisto
global rumoreCamminataColco
global rumoreScossaFreccia
global rumoreTempestaElettrica
global rumoreCuraRobo
global rumoreAntidoto
global rumoreAttPDifP
global rumoreAutoricarica
global rumoreRaffreddamento
global rumoreVelocizzaEfficienza
global suonoTeleColco
global suonoLancioOggetti
global suonoUsoPozione
global suonoUsoCaricabatterie
global suonoUsoMedicina
global suonoUsoBomba
global suonoUsoBombaVeleno
global suonoUsoEsca
global suonoUsoBombaAppiccicosa
global suonoUsoBombaPotenziata
global rumoreMovimentoNemiciPersonaggi
global rumoreAttaccoNemico
global rumoreLancioOggettoNemico
global rumoreMorteNemico
global suonoAperturaMappa
global rumoreScavare
global audioAmbienteSogno
global audioAmbienteCasaInterno
global audioAmbienteCasaEsterno
global audioAmbienteForesta
global audioAmbienteForestaFuoco
global canzoneSogno
global canzoneCasa
global canzoneForesta
global audioAmbienteStradaPerCitta1_notte
global audioAmbienteStradaPerCitta1_giorno
global audioAmbienteStradaPerCitta2_notte
global audioAmbienteStradaPerCitta2_giorno
global audioAmbienteStradaPerCitta3_notte
global audioAmbienteStradaPerCitta3_giorno
global canzoneEsternoCitta
global canzoneEsternoCasa
global rumoreBussareCitta
global rumoreSollevamentoPortaCitta
global canzoneCasaDavid
global audioAmbienteCasaDavid_notte
global audioAmbienteCasaDavid_giorno
global suonoaperturaporteCasaDavid
global suonochiusuraporteCasaDavid
global rumoreDoccia
global canzoneCitta
global audioAmbienteCitta_notte
global audioAmbienteCitta_giorno
global rumoreChiusuraPortaCitta


numSndTotali = 75
def caricaSuonoMostrandoAvanzamento(path):
    global numSndCaricatoTemp
    suono = CaricaFileProgetto.loadSound(path)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 0.5))
    numSndCaricatoTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 28) + ((GlobalHWVar.gpx * 3.0 / numSndTotali) * numSndCaricatoTemp)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(caricamentoCompiuto), GlobalHWVar.gpy * 0.5))
    GlobalHWVar.aggiornaSchermo()
    return suono

def loadSounds(numSndCaricato):
    global numSndCaricatoTemp
    numSndCaricatoTemp = numSndCaricato

    global selsta
    global selind
    global spostapun
    global selimp
    global selezione
    global spostaPunBattaglia
    global selObbiettivo
    global rumoreAttaccoSpada
    global rumoreLancioFreccia
    global rumoreAttaccoArco
    global rumoreParata
    global rumorecamminata
    global rumorelevelup
    global rumoreMorte
    global suonoaperturacofanetti
    global suonoaperturaporteForesta
    global suonochiusuraporteForesta
    global suonoaperturaporteCasa
    global suonochiusuraporteCasa
    global suonoRaccoltaEsca
    global suonoRaccoltaMonete
    global rumoreAcquisto
    global rumoreCamminataColco
    global rumoreScossaFreccia
    global rumoreTempestaElettrica
    global rumoreCuraRobo
    global rumoreAntidoto
    global rumoreAttPDifP
    global rumoreAutoricarica
    global rumoreRaffreddamento
    global rumoreVelocizzaEfficienza
    global suonoTeleColco
    global suonoLancioOggetti
    global suonoUsoPozione
    global suonoUsoCaricabatterie
    global suonoUsoMedicina
    global suonoUsoBomba
    global suonoUsoBombaVeleno
    global suonoUsoEsca
    global suonoUsoBombaAppiccicosa
    global suonoUsoBombaPotenziata
    global rumoreMovimentoNemiciPersonaggi
    global rumoreAttaccoNemico
    global rumoreLancioOggettoNemico
    global rumoreMorteNemico
    global suonoAperturaMappa
    global rumoreScavare
    global audioAmbienteSogno
    global audioAmbienteCasaInterno
    global audioAmbienteCasaEsterno
    global audioAmbienteForesta
    global audioAmbienteForestaFuoco
    global canzoneSogno
    global canzoneCasa
    global canzoneForesta
    global audioAmbienteStradaPerCitta1_notte
    global audioAmbienteStradaPerCitta1_giorno
    global audioAmbienteStradaPerCitta2_notte
    global audioAmbienteStradaPerCitta2_giorno
    global audioAmbienteStradaPerCitta3_notte
    global audioAmbienteStradaPerCitta3_giorno
    global canzoneEsternoCitta
    global canzoneEsternoCasa
    global rumoreBussareCitta
    global rumoreSollevamentoPortaCitta
    global canzoneCasaDavid
    global audioAmbienteCasaDavid_notte
    global audioAmbienteCasaDavid_giorno
    global suonoaperturaporteCasaDavid
    global suonochiusuraporteCasaDavid
    global rumoreDoccia
    global canzoneCitta
    global audioAmbienteCitta_notte
    global audioAmbienteCitta_giorno
    global rumoreChiusuraPortaCitta

    # suoni puntatore
    selsta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelSta.wav")
    selind = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelInd.wav")
    spostapun = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SpostaPun.wav")
    selimp = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelImp.wav")
    selezione = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/Selezione.wav")
    spostaPunBattaglia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SpostaPunBattaglia.wav")
    selObbiettivo = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelObbiettivo.wav")

    # suoni personaggio
    rumoreAttaccoSpada = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/AttaccoSpada.wav")
    rumoreLancioFreccia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/LancioFreccia.wav")
    rumoreAttaccoArco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/AttaccoArco.wav")
    rumoreParata = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/ParataConScudo.wav")
    rumorecamminata = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/Camminata.wav")
    rumorelevelup = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/Levelup.wav")
    rumoreMorte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/Morte.wav")

    # souno raccolta esca - monete
    suonoRaccoltaEsca = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/RaccoltaEsca.wav")
    suonoRaccoltaMonete = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/RaccoltaMonete.wav")
    rumoreAcquisto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Acquisto.wav")

    # suoni robo
    rumoreCamminataColco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Camminata.wav")
    rumoreScossaFreccia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/ScossaFreccia.wav")
    rumoreTempestaElettrica = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/TempestaElettrica.wav")
    rumoreCuraRobo = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Cura.wav")
    rumoreAntidoto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Antidoto.wav")
    rumoreAttPDifP = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/AttPDifP.wav")
    rumoreAutoricarica = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Autoricarica.wav")
    rumoreRaffreddamento = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Raffreddamento.wav")
    rumoreVelocizzaEfficienza = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/VelocizzaEfficienza.wav")

    # suono oggetti
    suonoTeleColco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/TeleColco.wav")
    suonoLancioOggetti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/LancioOggetti.wav")
    suonoUsoPozione = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Pozione.wav")
    suonoUsoCaricabatterie = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Caricabatterie.wav")
    suonoUsoMedicina = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Medicina.wav")
    suonoUsoBomba = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Bomba.wav")
    suonoUsoBombaVeleno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/BombaVeleno.wav")
    suonoUsoEsca = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Esca.wav")
    suonoUsoBombaAppiccicosa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/BombaAppiccicosa.wav")
    suonoUsoBombaPotenziata = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/BombaPotenziata.wav")

    # suoni nemici
    rumoreMovimentoNemiciPersonaggi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MovimentoNemiciPersonaggi.wav")
    rumoreAttaccoNemico = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/AttaccoVicinoNemico.wav")
    rumoreLancioOggettoNemico = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/AttaccoLontanoNemico.wav")
    rumoreMorteNemico = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MorteNemico.wav")

    # effetti speciali
    suonoaperturacofanetti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/AperturaCofanetto.wav")
    suonoAperturaMappa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/AperturaMappa.wav")
    rumoreScavare = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Scavare.wav")
    rumoreBussareCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/BussareCittà.wav")
    rumoreSollevamentoPortaCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SollevamentoPortaCittà.wav")
    rumoreChiusuraPortaCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/AbbassamentoPortaCittà.wav")
    rumoreDoccia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/DocciaCasaUfficiale.wav")

    # suoni apertura-chiusura porte
    suonoaperturaporteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaForesta.wav")
    suonochiusuraporteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaForesta.wav")
    suonoaperturaporteCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasa.wav")
    suonochiusuraporteCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasa.wav")
    suonoaperturaporteCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasaUfficiale.wav")
    suonochiusuraporteCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasaUfficiale.wav")

    # suoni sottofondi ambientali
    audioAmbienteSogno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Sogno.wav")
    audioAmbienteCasaInterno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaInterno.wav")
    audioAmbienteCasaEsterno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaEsterno.wav")
    audioAmbienteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Foresta.wav")
    audioAmbienteForestaFuoco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/ForestaFuoco.wav")
    audioAmbienteStradaPerCitta1_notte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1-notte.wav")
    audioAmbienteStradaPerCitta1_giorno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1-giorno.wav")
    audioAmbienteStradaPerCitta2_notte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2-notte.wav")
    audioAmbienteStradaPerCitta2_giorno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2-giorno.wav")
    audioAmbienteStradaPerCitta3_notte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3-notte.wav")
    audioAmbienteStradaPerCitta3_giorno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3-giorno.wav")
    audioAmbienteCitta_notte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Citta-notte.wav")
    audioAmbienteCitta_giorno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Citta-giorno.wav")
    audioAmbienteCasaDavid_notte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaUfficiale-notte.wav")
    audioAmbienteCasaDavid_giorno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaUfficiale-giorno.wav")

    # suoni canzoni
    canzoneSogno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/01-Sogno.wav")
    canzoneCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/02-Casa.wav")
    canzoneEsternoCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/03-EsternoCasaCittà.wav")
    canzoneForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/04-Foresta.wav")
    canzoneEsternoCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/03-EsternoCasaCittà.wav")
    canzoneCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/05-Città.wav")
    canzoneCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/06-CasaUfficiale.wav")
