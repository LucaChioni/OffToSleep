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
global suonoRaccoltaOggetto
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
global rumoreMovimentoNemici
global rumoreMovimentoPersonaggi
global rumoreAttaccoNemico
global rumoreLancioOggettoNemico
global rumoreMorteNemico
global suonoAperturaMappa
global rumoreScavare
global listaAudioAmbienteSogno
global listaAudioAmbienteCasaInterno
global listaAudioAmbienteCasaEsterno
global listaAudioAmbienteForesta
global listaAudioAmbienteForestaFuoco
global canzoneSogno
global canzoneCasa
global canzoneForesta
global listaAudioAmbienteStradaPerCitta1_notte
global listaAudioAmbienteStradaPerCitta1_giorno
global listaAudioAmbienteStradaPerCitta2_notte
global listaAudioAmbienteStradaPerCitta2_giorno
global listaAudioAmbienteStradaPerCitta3_notte
global listaAudioAmbienteStradaPerCitta3_giorno
global canzoneEsterniPacifici
global rumoreBussareCitta
global rumoreSollevamentoPortaCitta
global canzoneCasaDavid
global listaAudioAmbienteCasaDavid_notte
global listaAudioAmbienteCasaDavid_giorno
global suonoaperturaporteCasaDavid
global suonochiusuraporteCasaDavid
global rumoreDoccia
global canzoneCitta
global listaAudioAmbienteCitta_notte
global listaAudioAmbienteCitta_giorno
global rumoreChiusuraPortaCitta
global listaAudioAmbienteBiblioteca
global canzoneBiblioteca
global rumoreLancioPallaBibliotecario
global rumoreRitornoPallaBibliotecario
global rumoreAppoggioStrumentoEnigmi
global rumoreScorrimentoMatitaEnigmi
global rumoreScorrimentoGommaEnigmi
global rumoreCancellaTuttoEnigmi
global listaAudioAmbienteStradaPerSelva1
global listaAudioAmbienteStradaPerSelva2
global suonoaperturaporteSelva
global suonochiusuraporteSelva
global canzoneSelva
global listaAudioAmbienteSelva
global listaAudioAmbienteSelva_ultimaStanza
global listaAudioAmbienteAvamposto


numSndTotali = 101
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
    global suonoRaccoltaOggetto
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
    global rumoreMovimentoNemici
    global rumoreMovimentoPersonaggi
    global rumoreAttaccoNemico
    global rumoreLancioOggettoNemico
    global rumoreMorteNemico
    global suonoAperturaMappa
    global rumoreScavare
    global listaAudioAmbienteSogno
    global listaAudioAmbienteCasaInterno
    global listaAudioAmbienteCasaEsterno
    global listaAudioAmbienteForesta
    global listaAudioAmbienteForestaFuoco
    global canzoneSogno
    global canzoneCasa
    global canzoneForesta
    global listaAudioAmbienteStradaPerCitta1_notte
    global listaAudioAmbienteStradaPerCitta1_giorno
    global listaAudioAmbienteStradaPerCitta2_notte
    global listaAudioAmbienteStradaPerCitta2_giorno
    global listaAudioAmbienteStradaPerCitta3_notte
    global listaAudioAmbienteStradaPerCitta3_giorno
    global canzoneEsterniPacifici
    global rumoreBussareCitta
    global rumoreSollevamentoPortaCitta
    global canzoneCasaDavid
    global listaAudioAmbienteCasaDavid_notte
    global listaAudioAmbienteCasaDavid_giorno
    global suonoaperturaporteCasaDavid
    global suonochiusuraporteCasaDavid
    global rumoreDoccia
    global canzoneCitta
    global listaAudioAmbienteCitta_notte
    global listaAudioAmbienteCitta_giorno
    global rumoreChiusuraPortaCitta
    global listaAudioAmbienteBiblioteca
    global canzoneBiblioteca
    global rumoreLancioPallaBibliotecario
    global rumoreRitornoPallaBibliotecario
    global rumoreAppoggioStrumentoEnigmi
    global rumoreScorrimentoMatitaEnigmi
    global rumoreScorrimentoGommaEnigmi
    global rumoreCancellaTuttoEnigmi
    global listaAudioAmbienteStradaPerSelva1
    global listaAudioAmbienteStradaPerSelva2
    global suonoaperturaporteSelva
    global suonochiusuraporteSelva
    global canzoneSelva
    global listaAudioAmbienteSelva
    global listaAudioAmbienteSelva_ultimaStanza
    global listaAudioAmbienteAvamposto

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
    suonoRaccoltaOggetto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/RaccoltaOggetto.wav")
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

    # suoni nemici - personaggi
    rumoreMovimentoNemici = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MovimentoNemici.wav")
    rumoreMovimentoPersonaggi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MovimentoPersonaggi.wav")
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
    rumoreLancioPallaBibliotecario = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/LancioPallaBibliotecario.wav")
    rumoreRitornoPallaBibliotecario = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/RitornoPallaBibliotecario.wav")
    rumoreAppoggioStrumentoEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/AppaggioMatitaEnigmi.wav")
    rumoreScorrimentoMatitaEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/ScorrimentoMatitaEnigmi.wav")
    rumoreScorrimentoGommaEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/ScorrimentoGommaEnigmi.wav")
    rumoreCancellaTuttoEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/CancellaTuttoEnigmi.wav")

    # suoni apertura-chiusura porte
    suonoaperturaporteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaForesta.wav")
    suonochiusuraporteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaForesta.wav")
    suonoaperturaporteCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasa.wav")
    suonochiusuraporteCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasa.wav")
    suonoaperturaporteCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasaUfficiale.wav")
    suonochiusuraporteCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasaUfficiale.wav")
    suonoaperturaporteSelva = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaSelva.wav")
    suonochiusuraporteSelva = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaSelva.wav")

    # suoni sottofondi ambientali
    audioAmbienteSogno_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Sogno/Vento1.wav")
    audioAmbienteSogno_Vento2 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Sogno/Vento2.wav")
    listaAudioAmbienteSogno = [audioAmbienteSogno_Vento1, audioAmbienteSogno_Vento2]
    audioAmbienteCasaInterno_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaInterno/Vento1.wav")
    audioAmbienteCasaInterno_Cicale = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaInterno/Cicale.wav")
    listaAudioAmbienteCasaInterno = [audioAmbienteCasaInterno_Vento1, audioAmbienteCasaInterno_Cicale]
    audioAmbienteCasaEsterno_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaEsterno/Vento1.wav")
    audioAmbienteCasaEsterno_Cicale = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaEsterno/Cicale.wav")
    listaAudioAmbienteCasaEsterno = [audioAmbienteCasaEsterno_Vento1, audioAmbienteCasaEsterno_Cicale]
    audioAmbienteForesta_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/ForestaCadetta/Vento1.wav")
    audioAmbienteForesta_Cicale = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/ForestaCadetta/Cicale.wav")
    listaAudioAmbienteForesta = [audioAmbienteForesta_Vento1, audioAmbienteForesta_Cicale]
    audioAmbienteForesta_Fuoco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/ForestaCadetta/Fuoco.wav")
    listaAudioAmbienteForestaFuoco = [audioAmbienteForesta_Vento1, audioAmbienteForesta_Cicale, audioAmbienteForesta_Fuoco]
    audioAmbienteStradaPerCitta1_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1/Vento1.wav")
    audioAmbienteStradaPerCitta1_Cicale = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1/Cicale.wav")
    audioAmbienteStradaPerCitta1_Fuoco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1/Fuoco.wav")
    listaAudioAmbienteStradaPerCitta1_notte = [audioAmbienteStradaPerCitta1_Vento1, audioAmbienteStradaPerCitta1_Cicale, audioAmbienteStradaPerCitta1_Fuoco]
    listaAudioAmbienteStradaPerCitta1_giorno = [audioAmbienteStradaPerCitta1_Vento1, audioAmbienteStradaPerCitta1_Cicale]
    audioAmbienteStradaPerCitta2_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2/Vento1.wav")
    audioAmbienteStradaPerCitta2_Cicale = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2/Cicale.wav")
    audioAmbienteStradaPerCitta2_Fuoco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2/Fuoco.wav")
    listaAudioAmbienteStradaPerCitta2_notte = [audioAmbienteStradaPerCitta2_Vento1, audioAmbienteStradaPerCitta2_Cicale, audioAmbienteStradaPerCitta2_Fuoco]
    listaAudioAmbienteStradaPerCitta2_giorno = [audioAmbienteStradaPerCitta2_Vento1, audioAmbienteStradaPerCitta2_Cicale]
    audioAmbienteStradaPerCitta3_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3/Vento1.wav")
    audioAmbienteStradaPerCitta3_Fiume = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3/Fiume.wav")
    audioAmbienteStradaPerCitta3_Fuoco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3/Fuoco.wav")
    audioAmbienteStradaPerCitta3_Persone = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3/Persone.wav")
    listaAudioAmbienteStradaPerCitta3_notte = [audioAmbienteStradaPerCitta3_Vento1, audioAmbienteStradaPerCitta3_Fiume, audioAmbienteStradaPerCitta3_Fuoco]
    listaAudioAmbienteStradaPerCitta3_giorno = [audioAmbienteStradaPerCitta3_Vento1, audioAmbienteStradaPerCitta3_Fiume, audioAmbienteStradaPerCitta3_Persone]
    audioAmbienteCitta_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Citta/Vento1.wav")
    audioAmbienteCitta_Fuoco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Citta/Fuoco.wav")
    audioAmbienteCitta_Persone = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Citta/Persone.wav")
    listaAudioAmbienteCitta_notte = [audioAmbienteCitta_Vento1, audioAmbienteCitta_Fuoco]
    listaAudioAmbienteCitta_giorno = [audioAmbienteCitta_Vento1, audioAmbienteCitta_Persone]
    audioAmbienteCasaDavid_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaUfficiale/Vento1.wav")
    audioAmbienteCasaDavid_Persone = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/CasaUfficiale/Persone.wav")
    listaAudioAmbienteCasaDavid_notte = [audioAmbienteCasaDavid_Vento1]
    listaAudioAmbienteCasaDavid_giorno = [audioAmbienteCasaDavid_Vento1, audioAmbienteCasaDavid_Persone]
    audioAmbienteBiblioteca_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Biblioteca/Vento1.wav")
    audioAmbienteBiblioteca_Persone = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/Biblioteca/Persone.wav")
    listaAudioAmbienteBiblioteca = [audioAmbienteBiblioteca_Vento1, audioAmbienteBiblioteca_Persone]
    audioAmbienteStradaPerSelva_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerSelvaArida/Vento1.wav")
    audioAmbienteStradaPerSelva_Persone = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerSelvaArida/Persone.wav")
    audioAmbienteStradaPerSelva_Serpenti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/StradaPerSelvaArida/Serpenti.wav")
    listaAudioAmbienteStradaPerSelva1 = [audioAmbienteStradaPerSelva_Vento1, audioAmbienteStradaPerSelva_Persone]
    listaAudioAmbienteStradaPerSelva2 = [audioAmbienteStradaPerSelva_Vento1, audioAmbienteStradaPerSelva_Serpenti]
    audioAmbienteSelva_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/SelvaArida/Vento1.wav")
    audioAmbienteSelva_SerpentiVolAlto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/SelvaArida/SerpentiVolAlto.wav")
    audioAmbienteSelva_SerpentiVolBasso = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/SelvaArida/SerpentiVolBasso.wav")
    listaAudioAmbienteSelva = [audioAmbienteSelva_Vento1, audioAmbienteSelva_SerpentiVolAlto]
    listaAudioAmbienteSelva_ultimaStanza = [audioAmbienteSelva_Vento1, audioAmbienteSelva_SerpentiVolBasso]
    audioAmbienteSelva_Vento1 = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/AvampostoDiRod/Vento1.wav")
    audioAmbienteSelva_Serpenti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SottofondoPerZona/AvampostoDiRod/Serpenti.wav")
    listaAudioAmbienteAvamposto = [audioAmbienteSelva_Vento1, audioAmbienteSelva_Serpenti]

    # suoni canzoni
    canzoneSogno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/01-Sogno.wav")
    canzoneCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/02-Casa.wav")
    canzoneEsterniPacifici = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/03-EsterniPacifici.wav")
    canzoneForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/04-Foresta.wav")
    canzoneCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/05-Città.wav")
    canzoneCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/06-CasaUfficiale.wav")
    canzoneBiblioteca = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/07-Biblioteca.wav")
    canzoneSelva = caricaSuonoMostrandoAvanzamento("Risorse/Audio/Canzoni/08-SelvaArida.wav")
