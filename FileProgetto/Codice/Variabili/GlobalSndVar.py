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
global rumoreDialoghi
global suonoAperturaMappa
global rumoreScavare
global rumoreBussareCitta
global rumoreSollevamentoPortaCitta
global suonoaperturaporteCasaDavid
global suonochiusuraporteCasaDavid
global rumoreDoccia
global rumoreChiusuraPortaCitta
global rumoreLancioPallaBibliotecario
global rumoreRitornoPallaBibliotecario
global rumoreAppoggioStrumentoEnigmi
global rumoreScorrimentoMatitaEnigmi
global rumoreScorrimentoGommaEnigmi
global rumoreCancellaTuttoEnigmi
global suonoaperturaporteSelva
global suonochiusuraporteSelva


numSndTotali = 64
def caricaSuonoMostrandoAvanzamento(path):
    global numSndCaricatoTemp
    suono = CaricaFileProgetto.loadSound(path)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 0.5))
    numSndCaricatoTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 30) + ((GlobalHWVar.gpx * 1.0 / numSndTotali) * numSndCaricatoTemp)
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
    global rumoreDialoghi
    global suonoAperturaMappa
    global rumoreScavare
    global rumoreBussareCitta
    global rumoreSollevamentoPortaCitta
    global suonoaperturaporteCasaDavid
    global suonochiusuraporteCasaDavid
    global rumoreDoccia
    global rumoreChiusuraPortaCitta
    global rumoreLancioPallaBibliotecario
    global rumoreRitornoPallaBibliotecario
    global rumoreAppoggioStrumentoEnigmi
    global rumoreScorrimentoMatitaEnigmi
    global rumoreScorrimentoGommaEnigmi
    global rumoreCancellaTuttoEnigmi
    global suonoaperturaporteSelva
    global suonochiusuraporteSelva

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

    # suono dialoghi
    rumoreDialoghi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Dialoghi.wav")

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
